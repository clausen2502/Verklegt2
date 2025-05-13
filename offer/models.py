from django.db import models
from django.conf import settings
from property.models import Property

class PurchaseOffer(models.Model):
    OFFER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('contingent', 'Contingent'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='offers')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    message = models.TextField(blank=True)
    contingent_message = models.TextField(blank=True)
    offer_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=OFFER_STATUS_CHOICES, default='pending')
    expiration_date = models.DateField()

    def __str__(self):
        return f"Offer of ${self.amount} by {self.buyer.username} for {self.property}"
