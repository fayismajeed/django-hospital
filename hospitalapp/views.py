from django.shortcuts import render
from .models import Departments,Doctors
from .forms import BookingForm
# Create your views here.
def index(request):

    return render(request,'home.html')

def  about(request):
    return render(request,'about.html')

def doctors(request):
    dict_docts={
        'doctors' : Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docts)

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form = BookingForm()
    dict_form={
        'form' :form
    }
    return render(request,'booking.html',dict_form)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept' : Departments.objects.all()
        }
    return render(request,'dep.html',dict_dept)

