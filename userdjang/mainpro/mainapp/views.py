from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 

# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def logout_view(request):
    logout(request)
    return redirect('index')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect('index')
    else:
        return render(request,'register.html')
