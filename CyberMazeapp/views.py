from django.shortcuts import render,redirect
from .forms import ContactForm


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('contact')  # Redirect to a success page
    else:
        form = ContactForm()  # If the request is GET, render an empty form
    return render(request, 'contact.html', {'form': form})

def level1(request):
    return render(request,"level1.html")
def crypt1(request):
    return render(request,"crypt1.html")
def login(request):
    return render(request,"login.html")
def NS2(request):
    return render(request,"NS2.html")
def cloudrecon(request):
    return render(request,"cloud-recon.html")
def NS3(request):
    return render(request,"NS3.html")
def NS4(request):
    return render(request,"NS4.html")
def NS5(request):
    return render(request,"NS5.html")
def crypt2(request):
    return render(request,"crypt2.html")




