from django.shortcuts import redirect, render

from app1.forms import StudentForm
from app1.models import StudentRegistration

# Create your views here.

def home(request):
    return render(request, 'base.html')

def create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("Invalid Form")
    else:
        form = StudentForm()
    student = StudentRegistration.objects.all()
    return render(request, 'add.html', {'form': form, 'student': student})



def details(request, id):
    student = StudentRegistration.objects.get(id=id)
    form = StudentForm(instance=student)
    return render(request, 'details.html', {'student': student, 'form': form})



def update(request, id):
    student = StudentRegistration.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            print("Invalid Form")
    return render(request, 'update.html', {'student': student, 'form': form})

def delete(request, id):
    student = StudentRegistration.objects.get(id=id)
    student.delete()
    return redirect('create')