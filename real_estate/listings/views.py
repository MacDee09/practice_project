from django.shortcuts import render, redirect
from .models import Listings
from .forms import ListingsForm

def listing_list(request):
    listings = Listings.objects.all()
    context = {
        "listings": listings,
    }
    return render(request, "listings/listings.html", context)


def listing_retrieve(request, pk):
    listing = Listings.objects.get(id=pk)
    context = {
        "listing": listing,
    }
    return render(request, "listings/listing.html", context)


def listing_create(request):
    if request.method == "POST":
        form = ListingsForm(request.POST, )
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

        context = {
            "form": form 
        }

        return render(request,"listings/listing_create.html", context)


    form = ListingsForm()
    context = {
        "form" : form,
    }
    return render(request,"listings/listing_create.html", context)

def listing_update(request, pk):
    listing = Listings.objects.get(id=pk) 
    form = ListingsForm(instance = listing)

    if request.method == "POST":
        form = ListingsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
            "form": form 
        }

    return render(request,"listings/listing_update.html", context)

def listing_delete(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.delete()
    return redirect("/")