from django.shortcuts import render
from django.http import HttpResponse

def index(response):
	return HttpResponse("Hello, this is a test")
