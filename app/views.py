from django.shortcuts import render

from django.http import HttpResponse

from app.models import *

def Insert_Student(request):
    sn=input("enter stu name: ")
    sr=input('enter rno: ')
    sad=input('enter address: ')
    sag=input('enter age: ')
    sma=input('enter mailid: ')
    SO=Student.objects.get_or_create(sname=sn,srno=sr,sadd=sad,sage=sag,smail=sma)[0]
    SO.save()
    return HttpResponse('Student Inserted successfully')

def display_student(request):
    LOS=Student.objects.all()
    d={'student':LOS}
    return render(request,'display_student.html',context=d)


def Insert_Course(request):
    sn=input("enter stu name: ")
    sr=input('enter rno: ')
    sad=input('enter address: ')
    sag=input('enter age: ')
    sma=input('enter mailid: ')
    cnu=input('enter course number')
    cna=input('enter course name')
    cdu=input('enter duration')
    SO=Student.objects.get_or_create(sname=sn,srno=sr,sadd=sad,sage=sag,smail=sma)[0]
    SO.save()
    CO=Course.objects.get_or_create(srno=SO,cno=cnu,cname=cna,cdur=cdu)[0]
    CO.save()
    return HttpResponse('Course Inserted successfully')


def display_course(request):
    LOC=Course.objects.all()
    d={'course':LOC}
    return render(request,'display_course.html',context=d)




