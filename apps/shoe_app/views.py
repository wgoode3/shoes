from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "shoe_app/index.html")

def register(request):
    results = User.objects.register(request.POST)
    if results[0]:
        request.session["user_id"] = results[1].id
        return redirect("/shoes")
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect("/")

def login(request):
    results = User.objects.login(request.POST)
    if results[0]:
        request.session["user_id"] = results[1].id
        return redirect("/shoes")
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")

def shoes(request):
    if "user_id" not in request.session:
        messages.add_message(request, messages.ERROR, "You need to login first")
        return redirect("/")
    return render(request, "shoe_app/shoes.html")