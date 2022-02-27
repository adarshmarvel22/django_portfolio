from django.shortcuts import render,HttpResponse
from personal.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, 'Your Profile was created!')
    return render(request,'personal/index.html')

def about(request):
    return render(request,'personal/about.html')