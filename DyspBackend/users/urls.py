from django.conf.urls import url, include
from . import views

urlpatterns = [
	#user/1
	url(r'^(?P<user_id>[0-9]+)/$', views.us, name='us' )

]
