from django.db import models

# Create your models here.



class leader2(models.Model):
    name = models.CharField(max_length=100)
    points=models.IntegerField(default=0)