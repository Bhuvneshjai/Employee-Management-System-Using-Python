from django.contrib import admin
from api.models import Company, Employee

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','company_type',)
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','position',)
    list_filter = ('position',)

# Registered Here
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)