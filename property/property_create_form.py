from django import forms
from .models import Property

class PropertyCreateForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['seller', 'status']
        widgets = {
            'street_name': forms.TextInput(attrs={'class': 'form-control'}),
            'house_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'square_meters': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'custom_type': forms.TextInput(attrs={'class': 'form-control'}),
        }

