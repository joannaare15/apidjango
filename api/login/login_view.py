from django.shortcuts import render

# Create your views here.
def login_view(reques):
    template_name = "login.html"
    
    return render(reques,template_name)
