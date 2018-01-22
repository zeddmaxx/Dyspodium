from django.conf.urls import include, url
from . import views

urlpatterns = [
	#/question/
	url(r'^$', views.index, name='index'),

	#/question/12/
	url(r'^(?P<q_id>[0-9]+)/$', views.qs, name='qs'),
]