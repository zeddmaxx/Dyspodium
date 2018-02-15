from django.conf.urls import url
from DyspBackend.register import views as register_views

urlpatterns = [
    url(r'^signup/$', register_views.signup, name='signup'),
]