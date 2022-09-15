from django.db import models

# Create your models here.
class Users(models.Model):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_Active = models.BooleanField(default=True)
    created_On = models.DateTimeField(auto_now_add=True)
    updated_On = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name