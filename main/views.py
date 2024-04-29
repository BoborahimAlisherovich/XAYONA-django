

from django.shortcuts import render
from django.contrib import messages
# about_view,services_view,blog_view
def home_view(request):
    return render(request, "index.html" )

def about_view(request):
    return render(request, "about.html" )

def blog_view(request):
    return render(request, "blog.html" )

def services_view(request):
    return render(request, "services.html" )

