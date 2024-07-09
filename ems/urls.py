
from django.urls import path
from .views import add,addedEmp,deleteData,updateData,updateDone,viewEmp,empList,home

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('addedemp/',addedEmp,name='addedemp'),
    path('delete/<int:id>/',deleteData,name='delete_data'),
    path('update/<int:id>/',updateData,name='update_data'),
    path('update/<int:id>/',updateData,name='update_data'),
    path('view_emp/<int:id>/',viewEmp,name='view_emp'),
    path('updatedone/',updateDone,name='updatedone'),
    path('emplist/',empList,name='emplist'),
]