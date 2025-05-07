from django.db import models

class PurchaseOffer(models.Model):
    offer_price = models.FloatField()
    submitted_at = models.DateField()
    expiration_date = models.DateField()
    status = models.CharField(max_length=50)


# Create your models here.
