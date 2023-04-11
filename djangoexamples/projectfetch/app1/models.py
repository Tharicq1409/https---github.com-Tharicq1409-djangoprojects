from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    hire_date = models.DateField()
    department = models.CharField(max_length=50)
