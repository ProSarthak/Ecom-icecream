from email import message

from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.

def registerr(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken...")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken...")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                user.save()
                messages.success(request,"User created")
        
        else:
            messages.info(request,"Password did not match")
        return redirect('register.html')
        
    else:
        return render(request,'register.html')