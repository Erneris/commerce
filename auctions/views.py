from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User
from .models import Listing
from .models import watchlist

class createform(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Title'}))
    description = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Description'}))
    sbid = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Starting Bid'}))
    img = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Image URL'}))
    category = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Category'}))

class bid(forms.Form):
    id = forms.CharField(label="")
    bid = forms.CharField(label="")

def index(request):
    queryset = Listing.objects.values_list()
    return render(request, "auctions/index.html", {
    "query": queryset,
        })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        form = createform(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            sbid = form.cleaned_data["sbid"]
            category = form.cleaned_data["category"]
            img = form.cleaned_data["img"]
            listing = Listing(title = title, description = description, sbid = sbid, img = img, category = category)
            listing.save()
        else:
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            sbid = form.cleaned_data["sbid"]
            category = form.cleaned_data["category"]
            img = "https://media.istockphoto.com/photos/dotted-grid-paper-background-texture-seamless-repeat-pattern-picture-id1320330053?b=1&k=20&m=1320330053&s=170667a&w=0&h=XisfN35UnuxAVP_sjq3ujbFDyWPurSfSTYd-Ll09Ncc="
            listing = Listing(title = title, description = description, sbid = sbid, img = img, category = category, cbid = sbid)
            listing.save()
        response = redirect('/')
        return response
    else:
        return render(request, "auctions/create.html")
    
def listing(request, name):
    if request.method == "POST":
        form = bid(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            bid1 = form.cleaned_data["bid"]
            Listing.objects.filter(id = id).update(cbid = bid1)
            
            info = Listing.objects.filter(id = name)
            info = info[0]
            return render(request, "auctions/listing.html", {
            "query": info,
                })
    else:
        info = Listing.objects.filter(id = name)
        info = info[0]
        return render(request, "auctions/listing.html", {
        "query": info,
            })

@login_required(login_url='login')
def wladd(request, name):
    uid = request.user.username
    lid = name
    listing = watchlist(uid = uid, lid = lid)
    listing.save()

    return HttpResponseRedirect(reverse("index"))

@login_required(login_url='login')
def wl(request):
    items = watchlist.objects.filter(uid = request.user.username)
    products = []
    for item in items:
        products.append(Listing.objects.get(id=item.lid))
        
    return render(request, "auctions/watchlist.html",{
        "query": products
    })
    