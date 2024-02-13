# Generated by Django 5.0.2 on 2024-02-13 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0022_alter_parked_slot_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parked_slot',
            name='amount',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='parked_slot',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 8, 40, 46, 184446, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user_history',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 8, 40, 46, 185831, tzinfo=datetime.timezone.utc)),
        ),
    ]