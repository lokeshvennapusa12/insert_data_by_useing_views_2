from django.db import models

class Student(models.Model):
    sname=models.CharField(max_length=100)
    srno=models.IntegerField(primary_key=True)
    sadd=models.CharField(max_length=100)
    sage=models.IntegerField()
    smail=models.EmailField()

    def __str__(self):
        return str(self.srno)

class Course(models.Model):
    srno=models.ForeignKey(Student,on_delete=models.CASCADE)
    cno=models.CharField(max_length=100)
    cname=models.CharField(max_length=100)
    cdur=models.IntegerField()

    def __str__(self):
        return str(self.cno)
