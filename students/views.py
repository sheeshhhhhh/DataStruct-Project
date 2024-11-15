from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from students.form import StudentForm
from .models import Students

# Create your views here.
@csrf_exempt
def home(request):
    students = Students.objects.all()

    return render(request, 'home.html', { "students" : students })

@csrf_exempt
def createStudent(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'createStudents.html', { "form" : form })

def updateStudent(request, stdId):
    student = Students.objects.get(stdId=stdId)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit.html', { "form" : form })

def deleteStudent(request, stdId):
    student = Students.objects.get(stdId=stdId)
    student.delete()
    return redirect('home')