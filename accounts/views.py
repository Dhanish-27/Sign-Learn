from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def signup_user(request):
    if request.method == "POST":
        print("user is in post method")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirm_password = request.POST.get("pass2")

        # Validate input
        if not all([first_name, last_name, username, email, password, confirm_password]):
            error = "Please fill out all fields."
            return render(request, "signup.html", {"error": error})

        if password != confirm_password:
            error = "Passwords do not match."
            return render(request, "signup.html", {"error": error})

        # Check if user exists
        if User.objects.filter(username=username).exists():
            error = "Username already exists."
            return render(request, "signup.html", {"error": error})

        # Create user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            username=username
        )
        user.save()
        return redirect("login")
    else:
        return render(request, "signup.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error = "Invalid username or password."
            return render(request, "login.html", {"error": error})
    else:
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect(to="/")