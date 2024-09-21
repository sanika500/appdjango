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