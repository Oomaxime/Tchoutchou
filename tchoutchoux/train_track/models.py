from django.db import models


# Create your models here.

class Train(models.Model):
    trainID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    destination = models.TextField()
    date_start = models.CharField(max_length=30)
    date_end = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)
