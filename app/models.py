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

