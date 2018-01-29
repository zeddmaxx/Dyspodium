from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponse
from .models import Question, Answer
from .forms import UserForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy





def index(request):
	all_qs = Question.objects.all()
	context = {'all_qs':all_qs}
	return render(request, 'questions/index.html',context)

def qs(request, q_id):
	try:
		q = Question.objects.get(pk=q_id)
		ans = Answer.objects.get(question=q_id)

	except Question.DoesNotExist:
		raise Http404("Question does not exist!")

	return render(request, 'questions/qs.html',{'q':q, 'ans':ans})


class QuestionCreate(CreateView):
	model = Question
	fields = ['question', 'creator']

#class QuestionUpdate(UpdateView):
#	model = Question
#	fields = ['question', 'creator']
	



