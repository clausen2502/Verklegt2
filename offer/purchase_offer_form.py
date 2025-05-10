from django import forms
from .models import PurchaseOffer

class PurchaseOfferForm(forms.ModelForm):
    class Meta:
        model = PurchaseOffer
        fields = ['amount', 'message', 'expiration_date']

        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 89000000'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional note or condition...'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        labels = {
            'amount': 'Offer Amount (kr)',
            'message': 'Message / Contingency (optional)',
            'expiration_date': 'Offer Expiration Date',
        }
