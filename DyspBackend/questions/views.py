from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


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


