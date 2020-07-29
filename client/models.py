from django.db import models
from encoder import encoder


class Picture(models.Model):
    message = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='images/')
