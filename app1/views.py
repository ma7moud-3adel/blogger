from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Hi There, Welcome to Application 1 home.</h1>')

def profile(request):
	return HttpResponse('<h1>Hi There, Welcome to your Application 1 profile.</h1>')

def friends(request):
	return HttpResponse('<h1>Hi There</h1><br><h2>You can find your friends in this page</h2>')
