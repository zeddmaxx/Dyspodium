from django.conf.urls import include, url
from . import views

urlpatterns = [

        #login/
        url(r'^$', views.UserFormView.as_view(), name='register'),

    ]
