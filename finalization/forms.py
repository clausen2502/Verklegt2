from django import forms
import re

class ContactInfoForm(forms.Form):
    street_name = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=3, required=True)
    country = forms.CharField(max_length=100, required=True)
    kennitala = forms.CharField(max_length=10, min_length=10, required=True)

    def clean_postal_code(self):
        data = self.cleaned_data['postal_code']
        if not data.isdigit() or len(data) != 3:
            raise forms.ValidationError("Postal code must be exactly 3 digits.")
        return data

    def clean_kennitala(self):
        data = self.cleaned_data['kennitala']
        if not re.fullmatch(r'\d{10}', data):
            raise forms.ValidationError("Kennitala must be exactly 10 digits.")
        return data