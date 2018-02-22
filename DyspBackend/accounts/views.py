from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home(request):
	return render(request, 'accounts/home.html')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm()

		args = {'form': form}
	return render(request, 'accounts/reg_form.html', args)

def profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html', args)

def settings(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance = request.user)

		if form.is_valid:
			form.save()
			return redirect('/account/profile')

	else:
		form = EditProfileForm(instance = request.user)
		args = {'form': form}
		return render(request, 'accounts/settings.html', args)
