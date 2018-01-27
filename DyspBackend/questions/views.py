from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponse
from .models import Question, Answer
from .forms import UserForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView




def index(request):
	all_qs = Question.objects.all()

	context = {'all_qs':all_qs}
	return render(request, 'questions/index.html',context)

def qs(request, q_id):
	try:
		q = Question.objects.get(pk=q_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist!")
	return render(request, 'questions/qs.html',{'q':q})


class QuestionCreate(CreateView):
	model = Question
	fields = ['question', 'creator']
	



class UserFormView(View):
	form_class = UserForm
	template_name = 'questions/Signup/registration_form.html'

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
			usename = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username = usename, password = password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('questions:index')

		return render(request, self.template_name, {'form':form})