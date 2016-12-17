from django.shortcuts import render

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

    u = User.objects.filter(login=login,password=password)
    return HttpResponse(u)

