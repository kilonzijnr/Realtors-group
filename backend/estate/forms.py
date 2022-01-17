from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Property,Comments

#create your forms below

class CreateUserForm(UserCreationForm):
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

class PropertyForm(forms.ModelForm):
    """[property form class]
    Args:
        forms ([class]): [Class to create a form from the property model]
    """
    class Meta:
        model = Property
        fields = "__all__"

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = "__all__"

class RegisterForm(UserCreationForm):
    """Form for registering a new user"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']