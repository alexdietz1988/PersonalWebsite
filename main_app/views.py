from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post, Tag

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class Projects(TemplateView):
    template_name = "projects.html"

class Publications(TemplateView):
    template_name = "publications.html"

class Blog(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context