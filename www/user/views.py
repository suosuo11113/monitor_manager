from django.shortcuts import render_to_response
from django.http import  HttpResponse

# Create your views here.
def login(requst):
    return  HttpResponse("hello")