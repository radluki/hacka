from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send/(?P<login>[a-zA-Z]+)/(?P<password>[a-zA-Z]+)$', views.send, name='send'),
    url(r'^sendloc/(?P<login>[a-zA-Z]+)/(?P<password>[a-zA-Z]+)/(?P<longitude>[0-9]+)/(?P<latitude>[0-9]+)/$', views.sendloc, name='sendloc'),
    url(r'^register/(?P<login>[a-zA-Z]+)/(?P<password>[a-zA-Z]+)$',views.register,name='regiser'),
]
