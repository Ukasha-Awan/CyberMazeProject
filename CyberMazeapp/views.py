from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ContactForm



# Create your views here.
def index(request):
    return render(request,"index.html", {'username': request.user})
def blog(request):
    return render(request,"blog.html")
def about(request):
    return render(request,"about.html")
def domains(request):
    return render(request,"domains.html")
def levelList1(request):
    return render(request,"levelList1.html")
def levelList2(request):
    return render(request,"levelList2.html")
def levelList3(request):
    return render(request,"levelList3.html")
def levelList4(request):
    return render(request,"levelList4.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('/domains')  # Redirect to a success page
    else:
        form = ContactForm()  # Render an empty form for GET requests
    return render(request, 'contact.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        # Get username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists in the database
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in and redirect to the desired page
            login(request, user)
            messages.success(request, 'User logged in successfully')
            return redirect('/')  # Replace 'home' with the actual name of your view or URL
        else:
            # If user does not exist, create a new user and log them in
            try:
                new_user = User.objects.create_user(username=username, password=password)
                new_user.save()
                login(request, new_user)
                messages.success(request, 'New user created and logged in successfully')
                return redirect('/')  # Replace 'home' with the actual name of your view or URL
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")

    return render(request, 'login.html')

def level1(request):
    return render(request,"level1.html")
def crypt1(request):
    return render(request,"crypt1.html")

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
def NS6(request):
    return render(request,"NS6.html")
def crypt2(request):
    return render(request,"crypt2.html")
def crypt3(request):
    return render(request,"crypt3.html")
def crypt4(request):
    return render(request,"crypt4.html")
def trailoftroubles(request):
    return render(request,"trailoftroubles.html")





