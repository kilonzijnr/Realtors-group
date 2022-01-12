from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

#create your forms below

class CreateUserForm(UserCreationForm):
    """User Sign-up Form"""
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    """User update form"""
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """Profile update form"""
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']