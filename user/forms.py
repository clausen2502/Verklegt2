from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
import re


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError(
                "Username can only contain letters, numbers, and underscores (no spaces or special characters).")
        return username


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']

    def clean_profile_image(self):
        image = self.cleaned_data.get('profile_image')

        if image:
            if image.content_type not in ['image/jpeg', 'image/pjpeg']:
                raise forms.ValidationError("Only JPEG images are allowed.")

            if not image.name.lower().endswith(('.jpg', '.jpeg')):
                raise forms.ValidationError("File must end with .jpg or .jpeg.")

        return image

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r'^[A-Za-zÁÉÍÓÚÝÞÆÖáéíóúýþæö\- ]+$', first_name):
            raise forms.ValidationError("First name can only contain letters, hyphens, and spaces.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[A-Za-zÁÉÍÓÚÝÞÆÖáéíóúýþæö\- ]+$', last_name):
            raise forms.ValidationError("Last name can only contain letters, hyphens, and spaces.")
        return last_name


