from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.views.decorators.cache import never_cache

# Create your views here.
def register(request):
    if request.method =='POST':
        Username=request.POST['Username']
        email=request.POST['email']
        Password1=request.POST['Password1']
        Password2=request.POST['Password2']
        if Password1==Password2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                    messages.info(request,'email taken')
                    return redirect('register')
            else:
                user=User.objects.create_user(username=Username,password=Password1,email=email)
                user.save();
                messages.info(request,'User created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching..')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')
@never_cache
def login(request):
    if request.session.has_key('is_logged'):
        return redirect('/')
    if request.method=='POST':
        Username=request.POST['Username'] 
        Password=request.POST['Password']
        user=auth.authenticate(username=Username,password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect("results")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


    
def index(request):
    return render(request,'index.html')
