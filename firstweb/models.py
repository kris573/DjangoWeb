from django.db import models

# Create your models here.

class cal(models.Model):
    time = models.CharField(max_length=10)
    data = models.CharField(max_length=10)

