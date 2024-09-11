

# from django.shortcuts import render
# from.models import*
# def index (request):
#     if request.method=='POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         password=request.POST['password']
#         obj=details (name=name,email=email,password=password)
#         obj.save()
#     return render(request,'index.html')


from django.shortcuts import render,redirect
from.models import *
def index (request):
    mylist=['apple','grape','orange','banana']
    return render(request,'index.html',{'mylist':mylist})
def about(request):
    obj=details.objects.all()
    return render (request,'about.html',{'obj':obj})
    

