from rest_framework import serializers
from django.contrib.auth.models import User
from .models import parked_slot, parking_slot, user_history, user_review, reply


class User_api(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class Parked_slot_api(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = parked_slot

        
class Parking_slot_api(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = parking_slot


class User_history_api(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = user_history


class Review_api(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = user_review


class Reply_api(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = reply