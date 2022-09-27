from django.db import models

# Create your models here.
class Location(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length = 40)
    location = models.IntegerField()
