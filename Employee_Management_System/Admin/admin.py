from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

      list_display = ('name','fatherName','age','dob','department','address','phone','email','password','image')
