from django.shortcuts import render
from django.core import serializers
import json

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question, User
# ...

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(question)

def send(request, login, password):
    try:
        u = User.objects.filter(login=login,password=password)[0]
        all_users = User.objects.all()
        u_json = list()
        for k in all_users:
            tmp = {"login":k.login,"longitude":k.longitude,"latitude":k.latitude}
            u_json.append(tmp)
        u_json = json.dumps(u_json)
        #u_json = serializers.serialize('json', User.objects.all())
    except:
        u_json = 'Authentication failed'    
    
    return HttpResponse(u_json)

def sendloc(request, login, password,longitude,latitude):
    try:
        u = User.objects.filter(login=login,password=password)[0]
        u.longitude = longitude
        u.latitude = latitude
        u.save()
        data = [longitude,latitude]
    except:
        data = 'Authentication failed'    
    
    return HttpResponse(data)

def register(request,login,password)
    pass

