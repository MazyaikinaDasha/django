from django.shortcuts import render
from django.views.generic import TemplateView
from . models import *
def index(request):
	return render(request, 'mainApp/homePage.html')
def test(request):
	return render(request, 'mainApp/study.html', {'values': ['formula','theorem','eeee', '5555']})

	
   
	