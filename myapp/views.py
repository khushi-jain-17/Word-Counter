from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def operation(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    result=val1+val2
    return render(request,"result.html",{'result':result})

def  blog(request):
    return render(request,'blog.html',{'name':'Navin'})

def index(request):
    return render(request,'index.html')

def counter(request):
    text=request.POST['text']
    total = len(text.split())
    return render(request,"counter.html",{ 'total':total } )

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not the same")
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        else:
            messages.success(request,"Credentials Invalid")
            return redirect('login')
    else:    
        return render(request,'login.html')    

def logout_user(request):
    logout(request)
    return redirect('login')

def post(request,pk):
    return render(request,"post.html",{'pk':pk})

            
