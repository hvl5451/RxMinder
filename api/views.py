from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1> Welcome to the most rad API </h1>')


def process_image(request):
    # client_id = request.GET.get('client_id')
    image = request.body
    print(request.FILES)
    # print(client_id)
    if image:
        response = '<h1>Successful</h1>'
    else:
        response = '<h1>Failed</h1>'
    return HttpResponse(response)


# def getPillData(request, generics.ListAPI):

