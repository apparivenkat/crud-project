

from django import forms

from app1.models import StudentRegistration
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Enter Name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),
            'course' : forms.Select(attrs={'class':'form-control', 'placeholder':'Select Course'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'placeholder':'Select Gender'}),
            'phone' : forms.NumberInput(attrs={'maxlength':10, 'class':'form-control', 'placeholder':'Enter Mobile No'}),
            'dob' : forms.DateInput(attrs={'type':'date', 'class':'form-control', 'placeholder':'Enter Date of Birth'}),
            'age' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Age'}),
            'photo' : forms.FileInput(attrs={'class':'form-control', 'placeholder':'Upload Photo'}),
        }