"""RxMinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_image', views.process_image, name='image_process'),
    path('update', views.update_pill_data, name='update_db'),
    path('list_all', views.load_pill_data, name='load_pill_data'),
    path('delete', views.delete_pill_data, name='delete_pill'),
    path('alexa', views.process_alexa_result, name='alexa'),
]
