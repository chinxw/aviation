# Generated by Django 2.1.2 on 2018-10-24 10:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=4000)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 10, 24, 10, 34, 22, 634680, tzinfo=utc))),
                ('url', models.CharField(max_length=4000)),
                ('raw_data', models.CharField(max_length=4000)),
                ('category', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_given', models.CharField(max_length=128)),
                ('name_family', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='stat',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.User'),
        ),
    ]
