# Generated by Django 4.0.4 on 2022-06-29 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0002_alter_inbox_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 20, 55, 37, 76814)),
        ),
    ]
