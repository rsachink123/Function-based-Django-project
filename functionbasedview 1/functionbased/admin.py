from django.contrib import admin

from .models import Employee
class AdminEmployee(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company', 'email', 'salary', 'address','mobile']
admin.site.register(Employee, AdminEmployee)
