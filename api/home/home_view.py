from django.shortcuts import render

# Create your views here.
def home_view(reques):
    template_name = "index.html"

    return render(reques,template_name)
