from django import forms
import re
from datetime import datetime


class ContactInfoForm(forms.Form):
    street_name = forms.CharField(
        max_length=100,
        required=True,
        label="Street name"
    )
    city = forms.CharField(
        max_length=100,
        required=True,
        label="City"
    )
    postal_code = forms.CharField(
        max_length=3,
        required=True,
        label="Postal Code"
    )
    country = forms.CharField(
        max_length=100,
        required=True,
        label="Country"
    )
    kennitala = forms.CharField(
        max_length=10,
        required=True,
        label="National ID"
    )

    def clean_street_name(self):
        value = self.cleaned_data['street_name']
        if not re.match(r'^[\w\s\d]+$', value):
            raise forms.ValidationError("Street name may only contain letters, numbers, and spaces.")
        return value

    def clean_city(self):
        value = self.cleaned_data['city']
        if not re.match(r'^[A-Za-zÀ-ÿ\s\-]+$', value):
            raise forms.ValidationError("City may only contain letters.")
        return value

    def clean_postal_code(self):
        value = self.cleaned_data['postal_code']
        if not re.match(r'^\d{3}$', value):
            raise forms.ValidationError("Postal code must be 3 digits.")
        return value

    def clean_kennitala(self):
        value = self.cleaned_data['kennitala']
        if not re.match(r'^\d{10}$', value):
            raise forms.ValidationError("Kennitala must be 10 digits.")
        return value


class CreditCardForm(forms.Form):
    cardholder_name = forms.CharField(max_length=100)
    card_number = forms.CharField(max_length=19)
    expiry_date = forms.CharField(max_length=5)  # MM/YY
    cvc = forms.CharField(max_length=4)

    def clean_card_number(self):
        number = self.cleaned_data['card_number']
        if not re.fullmatch(r'\d{13,19}', number):
            raise forms.ValidationError("Card number must be 13–19 digits.")
        return number

    def clean_expiry_date(self):
        expiry = self.cleaned_data['expiry_date']
        if not re.match(r'^(0[1-9]|1[0-2])\/\d{2}$', expiry):
            raise forms.ValidationError("Expiry date must be in MM/YY format.")
        return expiry

    def clean_cvc(self):
        cvc = self.cleaned_data['cvc']
        if not re.fullmatch(r'\d{3,4}', cvc):
            raise forms.ValidationError("CVC must be 3 or 4 digits.")
        return cvc


class BankTransferForm(forms.Form):
    name = forms.CharField(max_length=100)
    account_number = forms.CharField(max_length=20)
    national_id = forms.CharField(max_length=10)
    description = forms.CharField(widget=forms.Textarea, required=False)
    amount = forms.DecimalField(min_value=0.01, max_digits=12, decimal_places=2)
    currency = forms.ChoiceField(choices=[
        ('ISK', 'ISK'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP')
    ])
    transfer_date = forms.DateField(required=False)  # No custom validation

    def clean_account_number(self):
        account = self.cleaned_data['account_number']
        if not re.fullmatch(r'\d{12}', account):
            raise forms.ValidationError("Account number must be exactly 12 digits.")
        return account

    def clean_national_id(self):
        kt = self.cleaned_data['national_id']
        if not re.fullmatch(r'\d{10}', kt):
            raise forms.ValidationError("National ID must be exactly 10 digits.")
        return kt
