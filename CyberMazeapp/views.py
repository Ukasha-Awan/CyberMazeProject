from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"index.html")
def blog(request):
    return render(request,"blog.html")
def about(request):
    return render(request,"about.html")
def domains(request):
    return render(request,"domains.html")
def contact(request):
    return render(request,"contact.html")
def level1(request):
    return render(request,"level1.html")
def crypt1(request):
    return render(request,"crypt1.html")
def login(request):
    return render(request,"login.html")
def NS2(request):
    return render(request,"NS2.html")
