from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
import json
# Create your views here.

# home view
def home(request):
    emp = Employee.objects.all()
    onleave = Employee.objects.filter(on_leave= True)
    emplength = emp.__len__
    available = Employee.objects.filter(on_leave= False)
    active = Employee.objects.filter(active= True)
    notactive = Employee.objects.filter(active= False)
    print(active)


    return render(request,'ems/home.html',{
        'emp':emp,
        'emplength':emplength,
        'onleaveemp':onleave,
        'onleave':onleave.__len__,
        'available':available.__len__,
        'active':active.__len__,
        'notactive':notactive.__len__
    })

# function to add the employee data
def add(request):
    print(request.method)
    if request.method == 'POST':
       form = EmployeeForm(request.POST )     
       if form.is_valid():
        onLeave = form.cleaned_data.get('on_leave')
        # leaveCount = form.cleaned_data.get('leave')
        # print(type(leaveCount),leaveCount)
        # print(onLeave,'onLeave')  
        formData = form.save(commit=True)
        if onLeave == True :
          formData.leave += 1
          print('employee leave incremented')
        form.save()
        form = EmployeeForm() 
       return redirect('/addedemp/', permanent=False)              
    else:
       print('else part') 
       form = EmployeeForm()      
    return render(request,'ems/add.html',{
        'form':form,
       })

def addedEmp(request):
    return render(request,'ems/added_emp.html')

def updateDone(request):
    return render(request,'ems/updatedone.html')

# function to update or edit data

# def update_data(request , id):
#     if request.method == 'POST':
#        print('update if') 
#        pi = Employee.objects.get(pk=id)
#        dataform =  EmployeeForm(request.POST ,instance=pi)
#        if dataform.is_valid():
#           dataform.save()                      
#        return render(request,'ems/update.html',{
#         'form':dataform
#        }) 

#     else:
#        print('update else') 
#        pi = Employee.objects.get(pk=id)
#        dataform =  EmployeeForm(instance=pi)
#        return render(request,'ems/update.html',{
#         'form':dataform
#        })


def updateData(request , id):
    emp = Employee.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        form = EmployeeForm(request.POST , instance=emp)
        if form.is_valid():
            onLeave = form.cleaned_data.get('on_leave')
            formData = form.save(commit=True)
            if onLeave == True :
               formData.leave += 1
               print('employee leave incremented')
            form.save()   
        return redirect('/updatedone')

    else:
        form = EmployeeForm(instance=emp)
        return render(request,'ems/update.html',{
        'form':form 
        
        })


#function to delete data

def deleteData(request, id):
    if request.method == 'POST':
        pi = Employee.objects.get(id=id)  # pk is primary key
        pi.delete()
        return redirect('/')   

def viewEmp(request, id):
    data = Employee.objects.get(id=id)
    # Employee.objects.filter(id = id).update(leave=10)
    # takingOnly = Employee.objects.filter(id=id).only('on_leave')  
    return render(request,'ems/view_emp.html',{
        'data':data,
        
         })

def empList(request):
    emp = Employee.objects.all()

    # emp = Employee.objects.filter(name__icontains='Kailas')
    # emplength = emp.__len__
    query = request.GET.get('query')
    if query : 
       emp = Employee.objects.filter(name__icontains=query)
    return render(request,'ems/emplist.html',{
        'emp':emp,
        'emplength':emp.__len__,
    })


