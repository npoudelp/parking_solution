# Generated by Django 5.0.2 on 2024-02-13 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0020_alter_parked_slot_parked_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parked_slot',
            name='amount',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='parked_slot',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 8, 25, 11, 624352, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user_history',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 8, 25, 11, 625761, tzinfo=datetime.timezone.utc)),
        ),
    ]
