from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class parking_slot(models.Model):
    slot_name = models.CharField(max_length=25)
    rate = models.FloatField()
    location = models.CharField(max_length=20)
    occupied = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f'{self.slot_name} | {self.location}'


class parked_slot(models.Model):
    slot_name = models.CharField(max_length=25, unique=True)
    parked_user = models.CharField(max_length=25 ,blank=True, null=False)
    paid = models.BooleanField(null=True, blank=True, default=False)
    parked_from = models.DateTimeField(default=timezone.now())
    parked_till = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.slot_name} | {self.parked_from}'


class user_history(models.Model):
    user_id = models.CharField(max_length=25)
    parked_from = models.DateTimeField(default=timezone.now())
    parked_till = models.DateTimeField(blank=True, null=True)
    park_fee = models.FloatField(blank=True, null=True)
    paid_amount = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.park_fee} | {self.park_date}'
    

class user_review(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.PROTECT)
    review = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.user_id}'
    

class reply(models.Model):
    admin_id = models.CharField(max_length=25, default='Parking Solution', editable=False)
    review_id = models.OneToOneField(user_review, on_delete=models.PROTECT)
    reply = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.admin_id} | {self.review_id} | {self.reply}'


# class admin_reply(models.Model):
    