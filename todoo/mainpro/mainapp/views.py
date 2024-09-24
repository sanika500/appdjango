# from django.shortcuts import render,redirect
# from .models import *
# # Create your views here.
# def index(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         obj=details(todo=name)
#         obj.save()
#         return redirect (index)
#     else:
#         obj=details.objects.all()
#         return render(request,'index.html',{'obj':obj})
# def delete_g(request,pk):
#     details_obj=details.objects.get(pk=pk)
#     details_obj.delete()
#     return redirect('index')  

from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        obj=details(todo=name)
        obj.save()
        return redirect (index)
    else:
        obj=details.objects.all()
        return render(request,'index.html',{'obj':obj})
def delete_g(request,pk):
    details_obj=details.objects.get(pk=pk)
    details_obj.delete()
    return redirect('index') 
def edit_g(request,pk):
    if request.method=='POST':
        title=request.POST.get('title')
        print(title)
        details.objects.filter(pk=pk).update(title=title)
        return redirect('index')
    else:
        todoobj=details.objects.all()
        data=details.objects.get(pk=pk)
        return render(request,'index.html',{'data':data,'todos':todoobj})



