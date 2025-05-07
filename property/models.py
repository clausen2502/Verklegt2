from django.db import models
from user.models import User

# Create your models here.
class Property(models.Model):
    street_name = models.CharField(max_length=100)
    house_number = models.IntegerField()
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    description = models.TextField()
    rooms = models.IntegerField()
    square_meters = models.IntegerField()
    status = models.BooleanField()
    type = models.CharField(max_length=100)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_date = models.DateField()

    def __str__(self):
        return f"{self.street_name} ({self.id})"


class PropertyPhoto(models.Model):
    image = models.CharField(max_length=4096)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='photos')

class PropertyType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type}"