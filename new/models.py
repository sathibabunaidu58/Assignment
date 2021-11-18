from django.db import models
from django.forms.widgets import DateInput, Widget



class Department(models.Model):
    branch=models.CharField(max_length=200)
    def __str__(self):
        return self.branch
class Details(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    faculty_name=models.CharField(max_length=200)
    date=models.DateField(auto_now=True,blank=True,null=True)
    


    def __str__(self):
        return self.faculty_name
    
