# Generated by Django 5.0.2 on 2024-02-12 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0010_alter_parked_slot_parked_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parked_slot',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 16, 24, 43, 357067, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user_history',
            name='parked_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 16, 24, 43, 358620, tzinfo=datetime.timezone.utc)),
        ),
    ]