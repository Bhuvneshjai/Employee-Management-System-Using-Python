# API Creation


## Versions
Django Version - 4.1.5
, Python Version - 3.9.6

## Terminal
In the terminal, firstly we start/create the project in current directory.
#### django-admin startproject <project_name>

when the project is created type in terminal to check the django project is working or not.
#### python manage.py runserver

if we want to change directory, then type in terminal
#### cd <folder_name> (exist_folder)

when we create/start the project, there are many files coming into the current folder such as -
#### urls.py , views.py , settings.py , models.py , asgi.py , wsgi.py , __init__.py , db.sqlite3 , manage.py , __pycache__

## Six Steps to create API:
### 1. Install Python , Django and Django Rest Framework
After Successfully Installed, We Check the JSON Response through API
In this we have two folder as
1. companyapi -> Default Folder
2. api

#### companyapi > urls.py
###### from .views import home_page
###### urlpatterns = [
######    path('admin/',admin.site.urls),
######    path('home/',home_page)
###### ]

--------------------------------------------------------------------------------------------------------------------------

###### from django.contrib import admin
###### from django.urls import path, include
###### from .views import home_page

###### urlpatterns = [
######     path('admin/', admin.site.urls),
######     path('home/',home_page),
######     path('api/v1/',include('api.urls'))
###### ]

#### companyapi > views.py
###### from django.http import HttpResponse
###### def home_page(request):
######    print("view.py is used to define the function which is used in the urls.py)
######    return HttpResponse("This is home page")

###### Terminal -> python manage.py runserver

--------------------------------------------------------------------------------------------------------------------------

###### from django.http import HttpResponse, JSONResponse
###### def home_page(request)
######     friends = [
######         'Miss Prabhi',
######         'Mr Bhuvi',
######         'Jain'
######     ]
######     return JSONResponse(friends, safe = False)

--------------------------------------------------------------------------------------------------------------------------

#### companyapi > settings.py 
###### INSTALLED APPS = [
######     ,'rest_framework'
######     ,'api'
###### ]


### 2. Set up Django Models
Create new folder which name is <api>

Terminal -> python manage.py startapp <folder_name> (api)

#### api > models.py
###### from django.db import models
###### class Company(models.Model):
######     company_id = models.AutoField(primary_key = True)
######     name = models.CharField(max_length = 50)
######     location = models.CharField(max_length = 50)
######     about = models.TextField()
######     company_type = models.CharField(max_length = 100, choices = (("it","Information Technology"),
######                                     ("non-it","Non Information Technology"),
######                                     ("mobile-phones","Mobiles Phones")))
######     added_date = models.DateTimeField(auto_now = True)
######     active = models.BooleanField(default = True)


### 3. Set up Serializers
#### api > serializers.py
###### from rest_framework import serializers
###### from api.models import Company
###### class CompanySerializer(serializers.HyperlinkedModelSerializer):
######     class Meta:
######         model = Company
######         fields = "__all__"

--------------------------------------------------------------------------------------------------------------------------

###### from rest_framework import serializers
###### from api.models import Company
###### class CompanySerializer(serializers.HyperlinkedModelSerializer):
######     company_id = serializers.ReadOnlyField() 
######     class Meta:
######         model = Company
######         fields = "__all__"


### 4. Set up Views
#### api > views.py
###### from django.shortcuts import render
###### from api.serializers import CompanySerializer
###### from rest_framework import viewsets
###### from api.models import Company
###### class CompanyViewSet(viewsets.ModelViewSet):
######     queryset = Company.objects.all()
######     serializer_class = CompanySerializer


### 5. Set up Urls
#### api > urls.py
###### from django. contrib import admin
###### from django.urls import path, include
###### from api.views import CompanyViewSet
###### from rest_framework import routers

###### router = routers.DefaultRouter()
###### router.register(r'companies',CompanyViewSet)

###### urlpatterns = [
######     path('',include(router.urls))
###### ]

After that - we go in the terminal, it is helpful to create table and connect with database
Terminal -> python manage.py makemigrations
         -> python manage.py migrate

### 6. Test your API'S
There are two method to test API
1. Postman Method
2. Browser Method