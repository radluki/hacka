from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getdata/(?P<login>[a-zA-Z]+)/(?P<password>[a-zA-Z]+)$', views.getdata, name='getdata'),
    url(r'^sendlocal/(?P<login>[a-zA-Z]+)/(?P<password>[a-zA-Z]+)/(?P<longitude>[0-9]+)/(?P<latitude>[0-9]+)/$', views.sendlocal, name='sendlocal'),
    url(r'^register/(?P<login>[a-zA-Z]+)/(?P<password>[a-zA-Z]+)$',views.register,name='regiser'),
]
