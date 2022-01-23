from django.shortcuts import render

from Admin.models import Employee
from .forms import EmployeeForm
# Create your views here.


def home(request):
    return render(request,'Admin/home.html')

def add(request):

    if request.method=='POST':
        form=EmployeeForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            form=EmployeeForm
            message='Employee Data is saved successfully'




    else:
        form=EmployeeForm

    return render(request,'Admin/add.html',{'form':form})

def show_data(request):

     employee=Employee.objects.all()

     return render(request,'Admin/viewemployee.html',{'emp':employee})

def delete_data(request,id):
    if request.method=='POST':

        pi=Employee.objects.get(pk=id)
        pi.delete()
        return render(request,'Admin/viewemployee.html')

def update_data(request,id):
    if request.method=='POST':

        pi=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()




    else:
        pi = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=pi)
    return render(request,'Admin/updateemployee.html',{'form':form})