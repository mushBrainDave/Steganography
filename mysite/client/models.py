from django.db import models


class Message(models.Model):
    message_text = models.CharField(max_length=200)

    def __str__(self):
        return self.message_text


class Picture(models.Model):
    #message = models.ForeignKey(Message, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='images/')
