from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello Django!")

def home_page(request):
    # return HttpResponse("Homepage Content")
    page = {"title": "Home Page", "content": "Welcome to the home page"}
    return render(request, "index.html", page)

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    email = "contact@example.com"
    social_profiles = [
        "Facebook: fb.me/example",
        "Instagram: instagram.com/example",
        "Linked-in: linked-in.com/example",
        "Youtube: youtube.com/channelid"
    ]
    hq = "r"
    return render(request, "contact.html", {"email_address": email, "socialprofiles": social_profiles, "hq": hq})

def order_page(request):
    return render(request, "order.html")

def experiment_page(request, person=None):
    if person is None:
        person = "Guest"
    return render(request, "experiment.html", {"data": person})