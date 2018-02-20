from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User

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
