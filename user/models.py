from django.db import models
from django.contrib.auth.models import User

class SellerUser(models.Model):
    SELLER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('agency', 'Real Estate Agency'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_type = models.CharField(max_length=20, choices=SELLER_TYPE_CHOICES)
    logo = models.ImageField(upload_to='seller_logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='seller_covers/', blank=True, null=True)
    bio = models.TextField(blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_seller_type_display()}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default_profile.png')

    def __str__(self):
        return self.user.username

