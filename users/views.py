from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth, update_session_auth_hash
from django.contrib import messages
from .forms import CustomRegistrationForm, CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form  = CustomRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Registered! Please Log In!")
            return redirect("login")
    else:
        form = CustomRegistrationForm()

    return render(request, "register.html", {"form":form})


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login_auth(request, user)
            messages.success(request, "Logged In!")
            return redirect("home")

        else:
            messages.error(request, "Invalid email or password!")

    return render(request, "login.html")

def logout(request):
    logout_auth(request)
    messages.success(request, "Logged out!")
    return redirect("login")

@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request, "Password Changed!")
            return redirect("home")
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {"form":form})

@login_required
def home(request):
    return render(request, "home.html")