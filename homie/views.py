from ast import Name
import email
import imp
from unicodedata import name
from django.shortcuts import render , HttpResponse , redirect
from datetime import datetime
from homie.models import Contact, IceCream
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib import messages


# Create your views here.
def index(request):
    
        objs = IceCream.objects.all()
        
    
        return render(request,"index.html",{'objs':objs})
    # return HttpResponse("This is homepage") 
def logout(request):
    auth.logout(request)
    return redirect("/")
    #return HttpResponse("This is about page")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully logged in !!!")
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,"login.html")
    #return HttpResponse("This is services page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your information has been submitted !!!') 
        return redirect('contact.html')
    else:
        return render(request,"contact.html") 
    #return HttpResponse("This is contact page")
    
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
                return redirect('login')
        
        else:
            messages.info(request,"Password did not match")
        return redirect('')
        
    else:
        return render(request,'register.html')
    

    
    
    