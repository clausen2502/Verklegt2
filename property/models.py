from django.db import models
from django.conf import settings

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('studio', 'Studio'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
    ]

    street_name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    description = models.TextField()
    square_meters = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES)
    custom_type = models.CharField(max_length=100, blank=True)  #Shown only if type == 'other'
    price = models.FloatField()
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing_date = models.DateField()
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)

    def get_type_display_name(self):
        if self.type == 'other' and self.custom_type:
            return self.custom_type
        return self.get_type_display()

    def __str__(self):
        return f"{self.street_name} ({self.get_type_display_name()})"



class PropertyPhoto(models.Model):
    image = models.ImageField(upload_to='property_photos/')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return f"Photo for {self.property}"
