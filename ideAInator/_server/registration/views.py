from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from core.models import myUser
from django.contrib.auth import get_user_model

# Create your views here.
def sign_up(req):
    User = get_user_model()

    if req.method == "POST":
        username = req.POST.get("email")  # Using email as the username
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists. Please choose a different email."}, status=400)

        try:
            user = User.objects.create_user(
                username=username,
                password=req.POST.get("password"),
                email=req.POST.get("email"),
                first_name=req.POST.get("first_name"),
                last_name=req.POST.get("last_name"),
            )

            # Custom logic for additional fields if necessary
            user.save()

            # Log in the user after successful creation
            login(req, user)
            return redirect("/")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return render(req, "registration/sign_up.html")
    
def sign_in(req):
    if req.method == "POST":
        user = authenticate(req, username=req.POST.get("email"), password=req.POST.get("password"))
        if user is not None:
            login(req, user)
            return redirect("/")
        
        # Add an error message to the context only after a failed attempt
        return render(req, "registration/sign_in.html", {"error": "Invalid email or password. Please try again."})
    
    # Render the form without error for the initial GET request
    return render(req, "registration/sign_in.html")


def logout_view(request):
    logout(request)
    return JsonResponse({"success": True })