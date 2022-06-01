from django.db import models
# Create your models here.

class StudentRegistration(models.Model):
    COURSE_CHOICES = [
        ('Computer Science', 'Computer Science'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Electronics Engineering', 'Electronics Engineering'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    name = models.CharField(max_length=100  )
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    phone = models.IntegerField()
    dob = models.DateField()
    age = models.IntegerField()
    photo = models.ImageField(upload_to='pics/')