from django.db import models

# Create your models here.

# Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    about = models.TextField()
    company_type = models.CharField(max_length = 100, choices = (("it","Information Technology"),
                                    ("non-it","Non Information Technology"),
                                    ("mobile-phones","Mobiles Phones")))
    added_date = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    # This method override the company object to company name 
    # This method helps us to give the actual name in the form
    def __str__(self):
        return self.name +", "+ self.location

# Employee Model
class Employee(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    position = models.CharField(max_length = 50, choices = (
        ('M','Manager'),
        ('SD','Software Developer'),
        ('PL','Project Leader')
    ))
    Company = models.ForeignKey(Company, on_delete = models.CASCADE)