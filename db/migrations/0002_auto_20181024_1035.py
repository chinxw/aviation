# Generated by Django 2.1.2 on 2018-10-24 10:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 10, 35, 20, 286430, tzinfo=utc)),
        ),
    ]
