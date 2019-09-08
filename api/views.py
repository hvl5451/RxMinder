from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from django.core.files.storage import default_storage
from . import imageProcessor
# Create your views here.


def index(request):
    return HttpResponse('<h1> Welcome to the most rad API </h1>')


def process_image(request):
    # client_id = request.GET.get('client_id')
    image = request.body
    print(request.FILES)
    file = request.FILES['fileToUpload']
    print('here')
    print(file.name)
    # print(client_id)

    print('here2')
    file_name123 = default_storage.save(file.name, file)

    # file_url = default_storage.url(final_file)
    imageProcessor.image_processing(file_name123)

    print('here3')
    if image:
        response = '<h1>Successful</h1>'
    else:
        response = '<h1>Failed</h1>'
    return HttpResponse(response)


# def getPillData(request, generics.ListAPI):

