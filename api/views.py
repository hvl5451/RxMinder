from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import PillDetails
from . import imageProcessor
import json
# Create your views here.


def index(request):
    return HttpResponse('<h1> Welcome to the most rad API </h1>')


def process_image(request):
    # client_id = request.GET.get('client_id')
    print(request.FILES)
    file = request.FILES['fileToUpload']
    print('here')
    print(file.name)
    # print(client_id)

    print('here2')
    file_name123 = default_storage.save(file.name, file)

    # file_url = default_storage.url(final_file)
    response = imageProcessor.image_processing(file_name123)

    print('here3')
    response = json.dumps(response)
    print(response)

    return HttpResponse(response)


def update_pill_data(request):
    data = request.body
    python_obj = json.loads(data)
    print(python_obj, flush=True)
    med = PillDetails(**python_obj)
    med.save()
    print(med, flush=True)l
    return HttpResponse('{"success": true}}')

# def getPillData(request, generics.ListAPI):

