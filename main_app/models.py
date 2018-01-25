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
    description = models.CharField(max_length=600)
    image = models.CharField(default = "",max_length=100)

    def __str__(self):
        return self.name

class Days(models.Model):
    name = models.CharField(max_length=100)
    day = models.IntegerField()
    diet = models.IntegerField()
    breakfast = models.CharField(max_length=100)
    lunch = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)

    def __str__(self):
        return self.name
