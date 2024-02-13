# Generated by Django 5.0.2 on 2024-02-13 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0029_user_history_paid_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parked_slot',
            name='occupied',
        ),
        migrations.AddField(
            model_name='parking_slot',
            name='occupied',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='parked_slot',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 10, 21, 58, 811947, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user_history',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 10, 21, 58, 813309, tzinfo=datetime.timezone.utc)),
        ),
    ]