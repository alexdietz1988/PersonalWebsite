from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Post, Tag

# Create your views here.
class Home(TemplateView):
    template_name = "portfolio/home.html"

class Projects(TemplateView):
    template_name = "portfolio/projects.html"

class Publications(TemplateView):
    template_name = "portfolio/publications.html"

class Blog(TemplateView):
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostDetail(TemplateView):
    template_name = "blog/post-detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=pk)
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text', 'tags']
    template_name = "blog/post-create.html"
    success_url = "/blog"