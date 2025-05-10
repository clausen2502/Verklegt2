from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
import re

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError(
                "Username can only contain letters, numbers, and underscores (no spaces or special characters).")
        return username