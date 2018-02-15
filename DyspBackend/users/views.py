from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def us(request, user_id):
	try:
		u = Profile.objects.get(pk=user_id)
	except UserInfo.DoesNotExist:
		raise Http404("User does not exist! ")
	return render(request, 'users/us.html', {'u' : u})

