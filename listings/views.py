from django.shortcuts import redirect, render
from .models import Listing
from .forms import ListingForm

# Create your views here.
# CRUDL = Create, Retrieve, Update, Delete, List


def listing_list(request):
    username = request.user.username
    listings = Listing.objects.all()

    template = "listings.html"
    context = {"listings": listings, 'username': username}
    return render(request, template, context)

def listing_retrive(request, pk):
    listing = Listing.objects.get(id=pk)

    template = "listing.html"
    context = {"listing": listing, 'user': request.user }
    return render(request, template, context)

def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    template = "listing_create.html"
    context = {"form": form}
    return render(request, template, context)

def listing_update(request,pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    template = "listing_update.html"
    context = {"form": form}
    return render(request, template, context)

def listing_delete(request,pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')