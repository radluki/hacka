from django.shortcuts import render
from django.core import serializers
import json
import django.utils.timezone as timezone 

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

from .models import Question, User
# ...

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(question)

def getdata(request, login, password):
    try:
        u = User.objects.filter(login=login,password=password)[0]
        all_users = User.objects.all()
        u_json = list()
        for k in all_users:
            tmp = {"login":k.login,"longitude":k.longitude,"latitude":k.latitude}
            u_json.append(tmp)
        #u_json = json.dumps(u_json)
        #u_json = serializers.serialize('json', User.objects.all())
    except Exception as e:
        u_json = ['Authentication failed']    
    
    return JsonResponse(u_json,safe=False)

def sendlocal(request, login, password,longitude,latitude):
    try:
        u = User.objects.filter(login=login,password=password)[0]
        u.longitude = longitude
        u.latitude = latitude
        u.date = timezone.now()
        u.save()
        data = [longitude,latitude]
    except Exception as e:
        data = ['Authentication failed']    
    
    return JsonResponse(data,safe=False)

def register(request,login,password):
    try:
        u = User.objects.filter(login=login)[0]
        message = 'User '+login+' already in database'
    except Exception as e:
        u = User(login=login, password=password,longitude=0,latitude=0,date=timezone.now())
        u.save()
        u = User.objects.filter(login=login)[0]
        message = {k:v for k,v in u.__dict__.items() if k!='_state'}

    return JsonResponse(message,safe=False)

