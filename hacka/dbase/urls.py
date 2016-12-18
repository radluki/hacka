from django.conf.urls import url

from . import views

GET_LOGIN_PASSWORD = '(?P<login>[a-zA-Z]+)/(?P<password>[a-zA-Z]+)'
GET_LL = '(?P<longitude>[+-]?(\d*\.\d+)|[+-]?\d+)/(?P<latitude>[+-]?(\d*\.\d+)|[+-]?\d+)'
INT_VAL = '(?P<id_val>[0-9]+)/(?P<login>[a-zA-Z]+)/(?P<question>[a-zA-Z]+)/(?P<answer>[a-zA-Z]+)'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getdata/'+GET_LOGIN_PASSWORD+'$', views.getdata, name='getdata'),
    url(r'^sendlocal/'+GET_LOGIN_PASSWORD+"/"+GET_LL+'$', views.sendlocal, name='sendlocal'),
    url(r'^register/'+GET_LOGIN_PASSWORD+'$',views.register,name='regiser'),
   
]
