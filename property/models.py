from django.db import models
from user.models import User

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.id})"


class PropertyPhoto(models.Model):
    image = models.CharField(max_length=4096)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='photos')

class PropertyType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type}"