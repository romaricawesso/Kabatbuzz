from django.shortcuts import render

# Create your views here.

def tableau_de_bord(request):
    return render(request, "index.html")
