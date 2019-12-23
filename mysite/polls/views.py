from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("sup, world. ur at the polls index.")

def detail(request, question_id):
  return HttpResponse("ur looking at quesion %s." % question_id)

def results(request, question_id):
  response = "ur looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("ur voting on question %s." % question_id)