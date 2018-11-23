from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect

from . import models
from . import forms

def index(request, t_id):
	cards = models.Card.objects.all().filter(top = t_id)
	return render(request, "cards/cards.html", {'card': cards})

def card_new (request):
	if request.method == "POST":
		card = models.Card()
		card.question = request.POST.get("question")
		card.answer = request.POST.get("answer")
		card.top = request.id
		card.save()
	return HttpResponseRedirect("new_card")

