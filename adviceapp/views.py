from django.shortcuts import render
from django.views import generic
from .models import Carearticle


"""Displays all articles in the browse articles page"""
class CarearticleList(generic.ListView):
    model = Carearticle
    queryset = Carearticle.objects.filter(approved_status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8