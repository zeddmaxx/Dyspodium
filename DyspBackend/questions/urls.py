from django.conf.urls import include, url
from . import views

app_name = 'question'


urlpatterns = [
	#/question/
	url(r'^$', views.index, name='index'),

	#/question/12/
	url(r'^(?P<q_id>[0-9]+)/$', views.qs, name='qs'),

	#/register/??
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/question/q/add/
    url(r'q/add/$', views.QuestionCreate.as_view(), name='question-add'),

]