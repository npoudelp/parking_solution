from django.contrib import admin
from .models import parked_slot, parking_slot, reply, user_review

# Register your models here.

admin.site.register(parking_slot)
admin.site.register(parked_slot)
admin.site.register(reply)
admin.site.register(user_review)