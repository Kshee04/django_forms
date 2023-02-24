from django.shortcuts import render
from djangoformsmorn.forms import StudentForm
# from djangoformsmorn import TeacherForm

def index(request):
    student=StudentForm()
    return render(request,'index.html',{'form':student})
# def teacher(request):
#     mwalimu=TeacherForm()
#     return render(request,'teachers.html',{'form':mwalimu})