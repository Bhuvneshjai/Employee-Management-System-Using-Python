from django.shortcuts import render
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework import viewsets
from api.models import Company, Employee
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

# Company View Set
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # for making this type of url https://127.0.0.1:8000/api/v1/companies/{id}/{method_name}
    # This means fetch all the data of employees which companies id is meention

    @action(detail = True, methods = ['get'])
    def employees(self, request, pk = None):
        print("Get Employees of ",pk," company")
        print("Method name will be passed in the url which is mention above and method name is (employees)")
        
        try:
            company = Company.objects.get(pk = pk)
            emps = Employee.objects.filter(Company = company)
            emp_serializers = EmployeeSerializer(emps, many = True, context = {'request' : request})
            return Response(emp_serializers.data)
        except Exception as e:
            print(e)
            return Response({
                'message' : 'Company might not exists !! Error'
            })

# Employee View Set
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer