from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views
from django.contrib.auth.views import login, logout

urlpatterns = [

	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$',views.profile, name='profile'),
]