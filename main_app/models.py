from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name
