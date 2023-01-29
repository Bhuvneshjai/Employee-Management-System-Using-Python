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
