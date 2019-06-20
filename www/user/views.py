from django.shortcuts import render_to_response
from django.http import  HttpResponse

# Create your views here.
def login(req):

    result = {'name':'suosuo','age':'23','grade':'80'}
    booklist = ["python","shell","c++","java"]

    return  HttpResponse(render_to_response('login.html',{'booklist':booklist,'result':result}))