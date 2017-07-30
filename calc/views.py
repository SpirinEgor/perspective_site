from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def make_form(request):
    return render(request, "calc_form.html", { "path": str(request.get_host())})

