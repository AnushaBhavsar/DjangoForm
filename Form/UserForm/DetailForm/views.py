from django.shortcuts import render
from django.http import HttpResponse
from .models import PM

# Create your views here.
def home(request):
    return render(request, 'form.html')

def saveData(request):
    p=PM()
    p.fname = request.GET.get('fname')
    p.lname = request.GET.get('lname')
    p.email = request.GET.get('email')
    p.contact_no = request.GET.get('contact_no')
    p.save()
    return HttpResponse('<center><h1>Data Saved</h1></center>')

def getData(request):
    data = PM.objects.all()
    dic={'fname':'Anu','lname':'Bhavsar'}
    return render(request, 'display.html', {'Data':data})

