# Generated by Django 2.1.2 on 2018-11-14 04:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20181107_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 4, 45, 24, 506050, tzinfo=utc)),
        ),
    ]