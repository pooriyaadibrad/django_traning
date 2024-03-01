from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
     return render(request=request, template_name='index.html',context={})


def data(request):
     user=models.User(Email="adibradp@gmail.com",Password="poo123456789")
     user.save()
     return render(request=request, template_name='data.html',context={})


def datatable(request):
     alldata=models.User.objects.all()
     return render(request=request, template_name='datatable.html',context={'alldata':alldata})