from django.shortcuts import render
from django.views.generic import DetailView
from .models import City


class CitiesDetailView(DetailView):
    """
        City detail view.
    """
    template_name = 'cities/city-detail.html'
    model = City

# Create your views here.
