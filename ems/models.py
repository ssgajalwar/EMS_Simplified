from django.db import models
# from django.contrib.admin.widgets import AdminDateWidget
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=120)
    dob = models.DateField()
    doj = models.DateField()
    dept = models.CharField(max_length=120,null=True,blank=True)
    post = models.CharField(max_length=120,null=True,blank=True) 
    address = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=120,null=True,blank=True)
    country = models.CharField(max_length=120,null=True,blank=True)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=120,null=True,blank=True)
    active = models.BooleanField()
    leave = models.IntegerField(null=True,blank=True,default=0)
    on_leave = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
