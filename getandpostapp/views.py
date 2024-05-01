from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,template_name="input.html")
def add(request):
    if request.method == "POST":
        x = int(request.POST.get("t1"))
        y = int(request.POST.get("t2"))
        z = x+y
        return HttpResponse(z)
    else:
        x = int(request.GET.get("t1"))
        y = int(request.GET.get("t2"))
        z = x + y
        return HttpResponse(z)