from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView, DetailView
from location.models import Location

def location_list(request):
    return render(request, 'location_list.html')

def person_location(request, pk):
    return render(request, 'person_location.html')