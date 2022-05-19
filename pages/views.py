from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    print(request.user)

    html = "<h1>This is my First Official Response {} <h1>".format(request.user)
    return HttpResponse(html)

# Create your views here.
def detailed_home_page(request):
    return render(request, "home.html", {})

# Create your views here.
def contactus_page(request):
    context = {
        "address" : "1122 Spring Hill Pwky",
        "phone" : "+1 770 380 9744",
        "email" : "reachus@h2kinfosys.com",
        "blog_numbers" : [1,101, 205, 303, 444, 556],
        }
    return render(request, "contactus.html", context)