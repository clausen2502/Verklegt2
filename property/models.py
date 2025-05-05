from django.db import models
from user.models import User

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

class UserPhoto(models.Model):
    image = models.CharField(max_length=4096)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)