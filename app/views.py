from django.shortcuts import render
from .models import Student,Teacher,Contractor

# Create your views here.
def fun(request):
    student_data=Student.objects.all()
    teacher_data=Teacher.objects.all()
    contractor_data=Contractor.objects.all()
    return render(request,'app/home.html',{'student_data':student_data,'teacher_data':teacher_data,'contractor_data':contractor_data})
