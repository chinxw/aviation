# Generated by Django 2.1.2 on 2018-10-24 10:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20181024_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 10, 47, 49, 866273, tzinfo=utc)),
        ),
    ]
