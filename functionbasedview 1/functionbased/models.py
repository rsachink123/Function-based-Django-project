from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    salary = models.IntegerField()
    address = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.first_name
