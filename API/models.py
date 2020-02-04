from django.db import models


class Response(models.Model):
    shape = models.CharField(max_length=10)
    low_size = models.FloatField()
    high_size = models.FloatField()
    color = models.CharField(max_length=1)
    clarity = models.CharField(max_length=4)
    caratPrice = models.FloatField()
    date = models.DateField()