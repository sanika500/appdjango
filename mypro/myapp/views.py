# from django.shortcuts import render,redirect
# from .models import*
# def index(request):
#     if request.POST:
#         title=request.POST.get('title')
#         todoobj=todoitem(title=title)
#         name=request.POST['name']
#         obj=details(name=name)
#         obj.save()
#         return redirect(index)
# obj=details.objects.all()

from django.shortcuts import render
from.models import*
def index (request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        obj=details (name=name,email=email,password=password)
        obj.save()
    return render(request,'index.html')



