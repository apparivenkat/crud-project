from django.contrib import admin

from app1.models import StudentRegistration

# Register your models here.
@admin.register(StudentRegistration)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','dob','age','photo', 'course', 'gender', 'phone']
    list_filter = ['name','email','dob','age','photo', 'course', 'gender', 'phone']
    search_fields = ['name','email','dob','age','photo', 'course', 'gender', 'phone']