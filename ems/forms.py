from django.core import validators
from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name',
            'dob',
            'doj',
            'dept',
            'post',
            'address',
            'city',
            'country',
            'zip_code',
            'state',
            'active',
            # 'leave',
            'on_leave'
        ]
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','type':'date'}),       
            'doj': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'dept': forms.TextInput(attrs={'class':'form-control'}),
            'post': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control address'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
            'active': forms.CheckboxInput(attrs={'class':'form-check'}),
            # 'leave': forms.TextInput(attrs={'class':'form-control','name':'leave','id':'leave'}),
            'on_leave': forms.CheckboxInput(attrs={'class':'form-check'}),
        }