from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Subscription, Inbox
# Create your views here.

def index(request):
    return render(request, "capstone/index.html")

def subscribe(request):
    if request.method=='POST':
        email = request.POST["email"]
        subscribe=Subscription.objects.create(email=email)
        subscribe.save()
    return HttpResponseRedirect(reverse("index"))

def feedback(request):
    if request.method=='POST':
        name= request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        inbox=Inbox.objects.create(name=name, email=email, subject=subject,message=message)
        inbox.save()
    return HttpResponseRedirect(reverse("index"))