from django.shortcuts import render,redirect
from django.core.cache import cache
from django.http import HttpResponse
from django.urls import reverse

from .forms import contactForm
from .models import contacts


def field(request):

    form =contactForm()
    return render(request, 'formdata.html', {'form': form})
    
def my_form(request):
    form = contactForm()
    if request.method == 'POST':

        form = contactForm(request.POST)
        if form.is_valid():

            """
            name=request.POST['name']
            email=request.POST['email']
            mobile=request.POST['mobile']
            Message=request.POST['Message']
            form2 = contact(name=name,email=email,mobile=mobile,Message=Message)
            form2.save()
           
            """
            form.save()
            return redirect('view')

def view_form(request):
    
            form3 = contacts.objects.all()
            return render(request, 'formview.html',{'form3': form3})
           

def del_form(request,id):
    
    form4 = contacts.objects.get(id=id)
    form4.delete()
    return redirect('view')






def update_form(request,id):

    if request.method == 'POST':
        form1 = contacts.objects.get(id=id)
        data=contactForm(request.POST,instance=form1)
        if data.is_valid():
            data.save()
            return redirect('view')
            
    else:
        form1 = contacts.objects.get(id=id)
        data=contactForm(instance=form1)
        return render(request,'formup.html',{'data':data})


 
   

      

def cache(request):
    return cache.clear()

