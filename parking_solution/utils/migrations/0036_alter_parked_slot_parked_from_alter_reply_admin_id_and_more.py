# Generated by Django 5.0.2 on 2024-02-13 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0035_alter_parked_slot_parked_from_alter_reply_admin_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parked_slot',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 16, 3, 20, 54437, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='admin_id',
            field=models.CharField(default='Parking Solution', editable=False, max_length=25),
        ),
        migrations.AlterField(
            model_name='user_history',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 16, 3, 20, 55753, tzinfo=datetime.timezone.utc)),
        ),
    ]
