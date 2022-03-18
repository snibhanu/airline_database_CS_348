from django.shortcuts import render
from django.http import HttpResponse
from .models import PassList
def homePageView(request):
    return HttpResponse("Hello, World!")
def index(response, id):
    ls = PassList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name,ls.address))
# Create your views here.
