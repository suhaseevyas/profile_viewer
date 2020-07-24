from django.shortcuts import render,redirect
from django.http import HttpResponse
from mysite.models import regi
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.db.models.signals import pre_save
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'index.html')


def register(request):   

    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname =  request.POST['lastname']
        email    =  request.POST['email']
        password =  request.POST['password']
        password2 = request.POST['password2']
        fileupload= request.FILES['fileupload']
        fs = FileSystemStorage()
        filename = fs.save(fileupload.name,fileupload)
        print(filename)
        upload = fs.url(filename)
        username = email

        if password!=password2:
            messages.error(request,"password does not match")
        register= regi(firstname=firstname, lastname=lastname, email=email, password=password, password2=password2, username=username,
        fileupload=upload)
        register.save()
        
        messages.success(request,"your account has been successfully created")
        return redirect('/')


def login(request):

    if request.method == 'POST':

        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']
       
        current_user = "dfg" 
        args = {}
        
        try: 
            current_user = regi.objects.get(email=loginemail, password= loginpassword)
            messages.success(request,'successfully Logged In ')
            args['current_user'] = current_user
            return render(request, 'new.html', args) 
        except regi.DoesNotExist:
            messages.error(request,'Invalid, try again !')
            return redirect('/')

    return HttpResponse('login')
    


