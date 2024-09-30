from django.db import models

# Create your models here.

from django.contrib.auth.models import User

types = (
    ('personal','PERSONAL'),
    ('Shopping', 'SHOPPING'),
    ('wishlist','WISHLIST'),
    ('work','WORK'),
    
    )

class todolist(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(default="Not completed",max_length=200)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    due_date = models.DateField(null=True)
    list = models.CharField(null=True,max_length=100)
   
    type = models.CharField(max_length=10, choices=types, default='personal',null=True)
   
