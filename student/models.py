from django.db import models
from django.contrib import admin

# Create your models here.

class StudentDetail(models.Model):
        name = models.CharField(max_length=250, help_text='Enter the student name')
        age = models.IntegerField(help_text="Enter age between 18 to 22")
        dob = models.DateField(help_text="Enter the date")
        reg_no = models.IntegerField(help_text="Enter the regster number")

class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ('name','age','dob','reg_no')