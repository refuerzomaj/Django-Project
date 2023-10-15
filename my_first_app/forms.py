from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email..'}))
    firstname = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your firtname..'}))
    lastname = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your lastname..'}))

class Meta:
    model = User
    fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2')
