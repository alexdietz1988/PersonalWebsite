from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class Projects(TemplateView):
    template_name = "projects.html"

class Publications(TemplateView):
    template_name = "publications.html"