from django.shortcuts import render,redirect
from registration.views import main

def homePage(request):
	return main(request)

def ourteam(request):
	return render(request, "ourteam.html" ,{})