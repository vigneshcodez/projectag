from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

class VerificationForm(forms.Form):
    code = forms.CharField(max_length=6)
