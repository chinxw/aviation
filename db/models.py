from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name_given = models.CharField(max_length=128)
    name_family = models.CharField(max_length=128)
    email = models.EmailField(max_length=255)

class Stat(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    tag = models.CharField(max_length=4000)
    date_entered = models.DateTimeField(default=timezone.now())
    url = models.CharField(max_length=4000)
    raw_data = models.CharField(max_length=4000)
    category = models.CharField(max_length=4000)
