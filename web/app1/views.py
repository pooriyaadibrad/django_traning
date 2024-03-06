from django.shortcuts import render
from . import models
from . import form
# Create your views here.
def index(request):
     return render(request=request, template_name='index.html',context={})


def data(request):
<<<<<<< HEAD
     form1=form.userForm()
     return render(request=request, template_name='formtest.html',context={'form':form1})
=======
     user=models.User(Email="adibradp@gmail.com",Password="poo123456789")
     user.save()
     return render(request=request, template_name='data.html')
>>>>>>> 5194c3f2f5d39d315c4f42f92eb650d630322568


def datatable(request):
     alldata=models.User.objects.all()
     return render(request=request, template_name='datatable.html',context={'alldata':alldata})

def saveData(request):
     if request.method=='POST':
          form2=form.userForm(request.POST)
          data=models.User(Email=form2.data['Email'],Password=form2.data['Password'])
          data.save()
          alldata = models.User.objects.all()
          return render(request=request,template_name='datatable.html',context={'alldata':alldata})