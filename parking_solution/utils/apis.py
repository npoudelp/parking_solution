from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import User_api, Parked_slot_api, Parking_slot_api, User_history_api, Review_api, Reply_api
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from .models import parking_slot, parked_slot, user_history, user_review, reply
from django.utils import timezone
from datetime import datetime
import datetime
from math import floor

# Create your views here.

class User_add(APIView):
    permission_classes = []

    def get(self, request):
        users = User.objects.all().order_by('-id')
        serialize = User_api(users, many=True)
        return Response(serialize.data, status=200)
    
    def post(self, request):
        try:
            new_user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
            new_user.first_name = request.data['first_name']
            new_user.last_name = request.data['last_name']
            new_user.save()
            return Response('user created', status=200)
        except:
            return Response('error creating user', status=400)
        

class User_login(APIView):
    permission_classes = []

    def get(self, request):
        return Response(status=200)

    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']

            user = authenticate(username=username, password=password)
            
            if user is not None:
                refresh = RefreshToken.for_user(user)
                login(request, user)
                return Response({
                    'username': request.data['username'],
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    },
                    status=200
                )
            else:
                return Response('invalid credentials', status=400)

        except:
            return Response('error getting user data', status=405)
        
class User_logout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            logout(request)
            return Response('logged out successfully', status=200)
        except:
            return Response('error loggin out', status=405)
        

class List_parking(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        total_slots = parking_slot.objects.all()
        serialize_total_slot =  Parking_slot_api(total_slots, many=True)
        used_slot = parked_slot.objects.all()
        serialize_used_slot = Parked_slot_api(used_slot, many=True)

        return Response({
            "slots" : serialize_total_slot.data
        },
        status=200)


class Book_slot(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        my_booking = parked_slot.objects.filter(parked_user=request.user)
        serialize = Parked_slot_api(my_booking, many=True)
        return Response({
            "my_booking": serialize.data,
            "message":"one user can book only one parking slot"
        }, status=200)
    
    def post(self, request):
        try:
            if parked_slot.objects.filter(parked_user=request.user).exists():
                return Response("you have existing booking", status=200)
            
            if parked_slot.objects.filter(slot_name=request.data['slot_name']).exists():
                return Response("parking slot is taken", status=200)

            book_slot = Parked_slot_api(data=request.data)
            if book_slot.is_valid(raise_exception=True):
                book_slot.save(parked_user=request.user)

                user_history.objects.create(user_id=request.user)

                update_slot = parking_slot.objects.get(id=request.data['slot_name'])         
                update_slot.occupied = True
                update_slot.save()

                return Response('booking successful', status=200)
            else:
                return Response('malformed data', status=400)
        except:
            return Response('error booking', status=400)


class Checkout(APIView):
    permission_classes = (IsAuthenticated,)

    def pay(request, parked_slot, occured_amount):
        if request.data['amount'] >= str(occured_amount):
            parked_slot.paid = True
            parked_slot.save()
            return True
        else:
            return False

    def get(self, request):
        try:
            get_parked_slot = parked_slot.objects.get(parked_user=request.user)
            serialize_parked = Parked_slot_api(get_parked_slot, many=False)

            get_parking_slot = parking_slot.objects.get(id=serialize_parked.data['slot_name'])
            serialize_parking = Parking_slot_api(get_parking_slot, many=False)

            current_time = timezone.now()

            delta_now = datetime.timedelta(days=current_time.day, hours=current_time.hour, minutes=current_time.minute, seconds=current_time.second)
            parked_time = get_parked_slot.parked_from
            delta_than = datetime.timedelta(days=parked_time.day, hours=parked_time.hour, minutes=parked_time.minute, seconds=parked_time.second)
            time_diff = delta_now - delta_than

            rate = serialize_parking.data['rate']
            hour_dif = time_diff.total_seconds()/3600
            amount = round((rate * hour_dif), 2)

            get_parked_slot.parked_till = current_time
            get_parked_slot.amount = amount
            get_parked_slot.save()

            my_booking = parked_slot.objects.filter(parked_user=request.user)
            serialize = Parked_slot_api(my_booking, many=True)
            return Response({
                "my_booking":serialize.data,
                "misc":{
                    "parking_duration": round(hour_dif, 3),
                    "warning": "hour is rounded upto three digit for simplicity",
                    "rate": rate,
                    "amount": amount
                    }
                }, status=200)
        
        except:
            return Response({
                "1":"your booking may not exixt",
                "2":"contact page admin to report error"
            }
            , status=400)

    
    def post(self, request):
        try:
            if not parked_slot.objects.filter(parked_user=request.user).exists():
                return Response("you don't have existing booking", status=400)
            

            get_parked_slot = parked_slot.objects.get(parked_user=request.user)
            serialize_parked = Parked_slot_api(get_parked_slot, many=False)

            amount = serialize_parked.data['amount']
            parked_till = serialize_parked.data['parked_till']

            if not serialize_parked.data['paid']:
                is_paid = Checkout.pay(request, get_parked_slot, amount)
                if not is_paid:
                    return Response("occured amount is greater tan paid amount", status=400)


            get_parked_slot.parked_till = parked_till
            get_parked_slot.amount = amount
            get_parked_slot.save()

            update_history = user_history.objects.filter(user_id=request.user).order_by('-id').first()
            update_history.parked_till = parked_till
            update_history.park_fee = amount
            update_history.paid_amount = request.data['amount']
            update_history.save()

            update_slot = parking_slot.objects.get(id=serialize_parked.data['slot_name'])         
            update_slot.occupied = False
            update_slot.save()

            get_parked_slot.delete()



            return Response("checkout successful" ,status=200)

        except:
            return Response({
                "1":"your booking may not exixt",
                "2":"contact page admin to report error"
            }
            , status=400)
        

class Review(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        try:
            get_review = user_review.objects.get(user_id=request.user.id)
            serialize_review = Review_api(get_review, many=False)

            get_reply = reply.objects.filter(review_id=serialize_review.data['id']).order_by('-id')
            serialize_reply = Reply_api(get_reply, many=True)

            return Response({
                "review": serialize_review.data,
                "reply": serialize_reply.data
            }, status=400)
        except:
            return Response("no review available")
        
    
    def post(self, request):
        try:
            if user_review.objects.filter(user_id=request.user.id).exists():
                review = user_review.objects.get(user_id=request.user.id)
                review.review = request.data['review']
                review.save()
                return Response("review updated")

            else:
                user_review.objects.create(review=request.data['review'], user_id=request.user)
                return Response("review added")

        except:
            return Response("error adding review", status=400)


#on during development
class delete(APIView):
    def post(self, request):
        # parked_slot.objects.all().delete()
        # user_history.objects.all().delete()
        user_review.objects.all().delete()
        return Response('parking slot empty', status=200)