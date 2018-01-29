from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    username = forms.CharField(max_length=100, required=False, help_text='Optional')
    location = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Please type a valid email address')
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['first_name','last_name','username','location','email','password']

