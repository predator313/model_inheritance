from django.db import models

# Create your models here.
#here we are going to see the concept of the 
#model inheritance
#the common_info is the abstract base class
class Common_info(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True

#now lets inherit the common_info in all the sub class
class Student(Common_info):
    # name=models.CharField(max_length=20)
    # age=models.IntegerField()
    date=None
    fees=models.IntegerField()

class Teacher(Common_info):
    # name=models.CharField(max_length=20)
    # age=models.IntegerField()
    # date=models.DateField()
    salary=models.IntegerField()

class Contractor(Common_info):
    # name=models.CharField(max_length=20)
    # age=models.IntegerField()
    #here the above field are by default inheritable
    #here we also modifies the data types
    date=models.DateTimeField()
    payment=models.IntegerField()

#lets see the concept of the multiple
#table inheritance this is also very useful ,this is like the concept of the forign key in the sql table and this is very use ful concept
class Exam_Center(models.Model):
    cname=models.CharField(max_length=20)
    city=models.CharField(max_length=30)

class Bacche(Exam_Center):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()

#proxy models inheritance concept
class A(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
class B(A):
    class Meta:
        #but ther is no proxy table
        proxy=True

