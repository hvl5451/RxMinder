from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import PillDetails
from . import imageProcessor
from django.core import serializers
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
    print(med, flush=True)
    return HttpResponse('{"success": true}}')

# def getPillData(request, generics.ListAPI):


def load_pill_data(request):
    # data = list(map(lambda x: x.__dict__, PillDetails.objects.all()))
    # data = serializers.dataSerializer(PillDetails.objects.all(), many=True)
    data = serializers.serialize('json', PillDetails.objects.all())
    print(data, flush=True)
    return HttpResponse(data, content_type=json)


def delete_pill_data(request):
    name = request.GET.get('medication_name')
    pill_instance = PillDetails.objects.get(medication_name=name)
    x = pill_instance.delete()
    print(x)
    return HttpResponse()

def process_alexa_result(request):
    pass
