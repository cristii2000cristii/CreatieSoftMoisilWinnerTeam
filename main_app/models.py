from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Diets(models.Model):
    name = models.CharField(max_length=100)
    foods = models.CharField(max_length=100)
    exercises = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.CharField(default = "",max_length=100)

    def __str__(self):
        return self.name
