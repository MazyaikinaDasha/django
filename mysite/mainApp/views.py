from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from . models import *
from django.views.generic import ListView,DetailView
from . import models
def index(request, t_id):
	cards = models.Card.objects.all().filter(top = t_id)
	return render(request, "mainApp/study.html", {'cards': cards})


	
   
	