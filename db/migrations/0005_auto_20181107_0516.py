# Generated by Django 2.1.2 on 2018-11-07 05:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_auto_20181026_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 5, 16, 2, 729235, tzinfo=utc)),
        ),
    ]
