from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_no']