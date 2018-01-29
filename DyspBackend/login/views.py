from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponse
from .models import Question, Answer
from .forms import UserForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
class UserFormView(View):
	form_class = UserForm
	template_name = 'login/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# Normalisation of data
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			location = form.cleaned_data['location']
			email = form.cleaned_data['password']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password = password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('question:index')

		return render(request, self.template_name, {'form':form})