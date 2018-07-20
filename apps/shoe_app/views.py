from django.shortcuts import render, redirect
from .models import User, Shoe, Purchase
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

    data = {
        "shoes": Shoe.objects.filter(bought=False)
    }
    return render(request, "shoe_app/shoes.html", data)

def dashboard(request, user_id):
    print(user_id)
    gained = 0.0
    spent = 0.0
    for shoe in Shoe.objects.filter(seller=user_id):
        if shoe.bought:
            gained += float(shoe.price)
    for purchase in Purchase.objects.filter(user=user_id):
        spent += float(purchase.shoe.price)

    data = {
        "bought_shoes": Purchase.objects.filter(user=user_id),
        "sold_shoes": Shoe.objects.filter(seller=user_id),
        "gained": gained,
        "spent": spent
    }
    return render(request, "shoe_app/dashboard.html", data)

def sell_shoes(request):
    results = Shoe.objects.sell(request.POST, request.session["user_id"])
    if not results[0]:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect("/dashboard/{}".format(request.session["user_id"]))

def buy_shoes(request, shoe_id):
    Shoe.objects.buy(shoe_id, request.session["user_id"])
    return redirect("/dashboard/{}".format(request.session["user_id"]))

def remove(request, shoe_id):
    Shoe.objects.get(id=shoe_id).delete()
    return redirect("/dashboard/{}".format(request.session["user_id"]))