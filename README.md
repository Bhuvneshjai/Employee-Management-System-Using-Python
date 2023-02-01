# API Creation


## Versions
Django Version - 4.1.5
, Python Version - 3.9.6

## Terminal
In the terminal, firstly we start/create the project in current directory.
# ---> django-admin startproject <project_name>

when the project is created type in terminal to check the django project is working or not.
# ---> python manage.py runserver

if we want to change directory, then type in terminal
# ---> cd <folder_name> (exist_folder)

when we create/start the project, there are many files coming into the current folder such as -
# ---> urls.py , views.py , settings.py , models.py , asgi.py , wsgi.py , __init__.py , db.sqlite3 , manage.py , __pycache__

## Six Steps to create API:
### 1. Install Python , Django and Django Rest Framework
After Successfully Installed, We Check the JSON Response through API
In this we have two folder as
1. companyapi -> Default Folder
2. api

#### companyapi > urls.py
###### from .views import home_page
###### urlpatterns = [
###### --------    path('admin/',admin.site.urls),
###### --------   path('home/',home_page)
###### -------- ]

--------------------------------------------------------------------------------------------------------------------------

###### from django.contrib import admin
###### from django.urls import path, include
###### from .views import home_page

###### urlpatterns = [
###### --------    path('admin/', admin.site.urls),
###### --------    path('home/',home_page),
###### --------    path('api/v1/',include('api.urls'))
###### -------- ]

#### companyapi > views.py
###### from django.http import HttpResponse
###### def home_page(request):
###### --------   print("view.py is used to define the function which is used in the urls.py)
###### --------   return HttpResponse("This is home page")

###### Terminal -> python manage.py runserver

--------------------------------------------------------------------------------------------------------------------------

###### from django.http import HttpResponse, JSONResponse
###### def home_page(request)
###### --------    friends = [
###### --------        'Miss Prabhi',
###### --------        'Mr Bhuvi',
###### --------        'Jain'
###### --------    ]
###### --------    return JSONResponse(friends, safe = False)

--------------------------------------------------------------------------------------------------------------------------

#### companyapi > settings.py 
###### INSTALLED APPS = [
###### --------    ,'rest_framework'
###### --------    ,'api'
###### -------- ]

###### When we put this we cannot create, update and delete api's
###### REST_FRAMEWORK = {
###### ---------    # ---> Use Django's standard `django.contrib.auth` permissions,
###### ---------    # ---> or allow read-only access for unauthenticated users.
###### ---------    # ---> When we put this we cannot update and delete api's
######
######     'DEFAULT_PERMISSION_CLASSES': [
###### --------        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
###### --------    ],
######
###### --------     # ---> You just need to remove the browsable API renderer from list of supported renderers for the view. The below code is used for remove the browsable api's. But it gives only in JSON.
###### --------    'DEFAULT_RENDERER_CLASSES': (
###### --------        'rest_framework.renderers.JSONRenderer',
###### --------    )
###### -------- }


### 2. Set up Django Models
Create new folder which name is <api>

Terminal -> python manage.py startapp <folder_name> (api)

#### api > models.py
###### from django.db import models
###### # ---> Company Model
###### class Company(models.Model):
###### --------     company_id = models.AutoField(primary_key = True)
###### --------     name = models.CharField(max_length = 50)
###### --------     location = models.CharField(max_length = 50)
###### --------     about = models.TextField()
###### --------     company_type = models.CharField(max_length = 100, choices = (("it","Information Technology"),
###### --------                                     ("non-it","Non Information Technology"),
###### --------                                     ("mobile-phones","Mobiles Phones")))
###### --------     added_date = models.DateTimeField(auto_now = True)
###### --------     active = models.BooleanField(default = True)

######    # ---> This method override the company object to company name 
######    # ---> This method helps us to give the actual name in the form
###### --------     def __str__(self):
###### --------  --------      return self.name +", "+ self.location
######
###### # ---> Employee Model
###### class Employee(models.Model):
###### --------    name = models.CharField(max_length = 100)
###### --------    email = models.CharField(max_length = 50)
###### --------    address = models.CharField(max_length = 100)
###### --------    phone = models.CharField(max_length = 10)
###### --------    position = models.CharField(max_length = 50, choices = (
###### --------        ('M','Manager'),
###### --------        ('SD','Software Developer'),
###### --------        ('PL','Project Leader')
###### --------    ))
###### --------    Company = models.ForeignKey(Company, on_delete = models.CASCADE)


### 3. Set up Serializers
#### api > serializers.py
###### from rest_framework import serializers
###### from api.models import Company
###### class CompanySerializer(serializers.HyperlinkedModelSerializer):
###### --------     class Meta:
###### --------      -------   model = Company
###### --------      -------   fields = "__all__"

--------------------------------------------------------------------------------------------------------------------------

###### from rest_framework import serializers
###### from api.models import Company
###### class CompanySerializer(serializers.HyperlinkedModelSerializer):
###### --------     company_id = serializers.ReadOnlyField() 
###### --------     class Meta:
###### --------     ------    model = Company
###### --------     ------    fields = "__all__"

--------------------------------------------------------------------------------------------------------------------------

###### from rest_framework import serializers
###### from api.models import Company, Employee
###### 
###### # ---> Company Serializers
###### class CompanySerializer(serializers.HyperlinkedModelSerializer):
###### --------    company_id = serializers.ReadOnlyField()
###### --------    class Meta:
###### --------    ------    model = Company
###### --------    ------    fields = "__all__"

###### # ---> Employee Serializers
###### class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
###### --------    id = serializers.ReadOnlyField()
###### --------    class Meta:
###### --------    ------    model = Employee
###### --------    ------    fields = "__all__"


### 4. Set up Views
#### api > views.py
###### from django.shortcuts import render
###### from api.serializers import CompanySerializer
###### from rest_framework import viewsets
###### from api.models import Company
###### class CompanyViewSet(viewsets.ModelViewSet):
###### --------     queryset = Company.objects.all()
###### --------     serializer_class = CompanySerializer

--------------------------------------------------------------------------------------------------------------------------

###### from django.shortcuts import render
###### from api.serializers import CompanySerializer, EmployeeSerializer
###### from rest_framework import viewsets
###### from api.models import Company, Employee
###### from rest_framework.decorators import action
###### from rest_framework.response import Response
###### 
###### # ---> Create your views here.
###### 
###### # ---> Company View Set
###### class CompanyViewSet(viewsets.ModelViewSet):
###### --------    queryset = Company.objects.all()
###### --------    serializer_class = CompanySerializer
###### 
######     # ---> for making this type of url https://127.0.0.1:8000/api/v1/companies/{id}/{method_name}
######     # ---> This means fetch all the data of employees which companies id is meention
###### 
###### --------    @action(detail = True, methods = ['get'])
###### --------    def employees(self, request, pk = None):
###### --------    -------    print("Get Employees of ",pk," company")
###### --------    -------    print("Method name will be passed in the url which is mention above and method name is (employees)")
######         
###### --------    -------    try:
###### --------    -------    ------- company = Company.objects.get(pk = pk)
###### --------    -------    ------- emps = Employee.objects.filter(Company = company)
###### --------    -------    -------    emp_serializers = EmployeeSerializer(emps, many = True, context = {'request' : request})
###### --------    -------    -------    return Response(emp_serializers.data)
###### --------    -------    except Exception as e:
###### --------    -------    -------    print(e)
###### --------    -------    -------    return Response({
###### --------    -------    -------        'message' : 'Company might not exists !! Error'
###### --------    -------    -------    })
###### 
###### # ---> Employee View Set
###### class EmployeeViewSet(viewsets.ModelViewSet):
###### --------    queryset = Employee.objects.all()
###### --------    serializer_class = EmployeeSerializer


### 5. Set up Urls
#### api > urls.py
###### from django. contrib import admin
###### from django.urls import path, include
###### from api.views import CompanyViewSet, EmployeeViewSet
###### from rest_framework import routers

###### router = routers.DefaultRouter()
###### router.register(r'companies',CompanyViewSet)
###### router.register(r'employees',EmployeeViewSet)

###### urlpatterns = [
###### --------     path('',include(router.urls))
###### -------- ]

After that - we go in the terminal, it is helpful to create table and connect with database
Terminal -> python manage.py makemigrations
         -> python manage.py migrate

### 6. Test your API'S
There are two method to test API
1. Postman Method
2. Browser Method