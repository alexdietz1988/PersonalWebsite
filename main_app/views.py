from datetime import datetime
from django.views import View
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from .models import Post, Tag, Comment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
        context['tags'] = Tag.objects.all()
        context['posts'] = Post.objects.all()
        return context

class PostDetail(TemplateView):
    template_name = "blog/post-detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=pk)
        context['tags'] = Tag.objects.all()
        return context

class AddComment(View):
    def post(self, request, pk):
        user = self.request.user
        body = request.POST.get("body")
        post = Post.objects.get(pk=pk)
        Comment.objects.create(user=user, body=body, post=post, created_at=datetime.now)
        return redirect('blog')


class TaggedPosts(TemplateView):
    template_name = "blog/tagged-posts.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(pk=pk)
        context['posts'] = Post.objects.filter(tags = pk)
        return context

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/blog")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)