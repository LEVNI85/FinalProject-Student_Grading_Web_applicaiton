from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

user = get_user_model()

class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['email', 'password1', 'password2']

    widgets = {
        'email' : forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder': 'Enter your email'}),
        'password1' : forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder': 'Enter your password'}),
        'password2' : forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm your password'})
    }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder':'Enter your old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder':'Enter your new password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder':'Confirm your new password'}))
    
