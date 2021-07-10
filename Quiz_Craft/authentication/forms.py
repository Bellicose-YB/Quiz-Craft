from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class' : "form-control"}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class' : "form-control"}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class' : "form-control"}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class' : "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs = {'class' : "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs = {'class' : "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class' : "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs = {'class' : "form-control"}))

    class Meta:
        model = User
        fields = ('username','password', )