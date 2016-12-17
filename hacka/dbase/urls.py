from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send/(?P<login>[a-zA-Z]+)/(?P<password>[a-zA-Z]+)$', views.send, name='send'),
]
