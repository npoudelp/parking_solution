from django.urls import path
from . import apis


appname = 'utils'
urlpatterns = [
    path('', apis.User_add.as_view(), name='utils_user_add'),
    path('login/', apis.User_login.as_view(), name='utils_user_login'),
    path('logout/', apis.User_logout.as_view(), name='utils_user_logout'),
    path('get_slot/', apis.List_parking.as_view(), name='util_list_parking'),
    path('book_slot/', apis.Book_slot.as_view(), name='util_book_slot'),
    path('checkout/', apis.Checkout.as_view(), name='utils_checkout'),
    path('review/', apis.Review.as_view(), name='utils_review'),
    path('delete/', apis.delete.as_view()),
]