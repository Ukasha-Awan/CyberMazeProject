from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
def base(request):
    return render(request,"base.html")

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
                # messages.success(request, 'New user created and logged in successfully')
                return redirect('/')  # Replace 'home' with the actual name of your view or URL
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")

    return render(request, 'login.html')

def user_logout(request):
    if request.method == 'POST':  # Logout should be triggered via POST for security
        logout(request)  # Logs the user out
        messages.success(request, "Logged out successfully!")
        return redirect('/login')  # Redirect to the home page or login page

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

#===========================================================
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import UserScore
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
@login_required
def update_score(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            success = data.get("success")  # Boolean indicating task success

            # Debugging: Log received data
            print(f"Received data: {data}")

            if success is None:
                return JsonResponse({"error": "Invalid input"}, status=400)

            # Fetch or create user score object
            user_score, _ = UserScore.objects.get_or_create(user=request.user)

            # Update score based on success
            if success:
                user_score.score += 5
            else:
                user_score.score -= 3  # Penalty for failure

            # Ensure score doesn't drop below zero
            if user_score.score < 0:
                user_score.score = 0

            # Determine pass or fail based on score
            if user_score.score > 30:
                user_score.result = 'pass'
                user_score.level = (user_score.level or 1) + 1  # Increment level if undefined set it to 1
            else:
                user_score.result = 'fail'
                if user_score.level > 1:
                    user_score.level = 1  # Reset level to 1 if failed

            user_score.save()

            # Debugging: Log updated user score
            print(f"Updated user score: {user_score.score}, result: {user_score.result}, level: {user_score.level}")

            return JsonResponse({
                "message": "Score updated!",
                "score": user_score.score,
                "result": user_score.result,
                "level": user_score.level
            })

        except (ValueError, KeyError) as e:
            return JsonResponse({"error": f"Invalid data format: {str(e)}"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@login_required
def get_score(request):
    user_score = get_object_or_404(UserScore, user=request.user)
    return JsonResponse({"username": request.user.username, "score": user_score.score})




#==========================================================================
# class TeamListView(LoginRequiredMixin, ListView):
#     model = Team
#     template_name = "team_list.html"
#     context_object_name = "teams"
#     login_url = "login/"





