from django.db import models


# Create your models here.
class Reading(models.Model):
    temp = models.CharField(max_length=5)
    temp_min = models.CharField(max_length=5)
    temp_max = models.CharField(max_length=5)
    pressure = models.IntegerField()
    humidity = models.CharField(max_length=5)
    last_update = models.DateTimeField()

