from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
        context['tags'] = Tag.objects.all()
        context['posts'] = Post.objects.all()
        return context

class PostDetail(TemplateView):
    template_name = "blog/posts/post-detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=pk)
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body', 'tags']
    template_name = "blog/posts/post-create.html"
    success_url = "/blog"

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body', 'tags']
    template_name = "blog/posts/post-update.html"
    success_url = "/blog"

class PostDelete(DeleteView):
    model = Post
    template_name = "blog/posts/post-delete.html"
    success_url = "/blog"

class TagList(TemplateView):
    template_name = "blog/tags/tag-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class TagCreate(CreateView):
    model = Tag
    fields = ['name']
    template_name = "blog/tags/tag-create.html"
    success_url = "/tags"

class TagUpdate(UpdateView):
    model = Tag
    fields = ['name']
    template_name = "blog/tags/tag-update.html"
    success_url = "/tags"

class TagDelete(DeleteView):
    model = Tag
    template_name = "blog/tags/tag-delete.html"
    success_url = "/tags"

class TaggedPosts(TemplateView):
    template_name = "blog/tags/tagged-posts.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(pk=pk)
        context['posts'] = Post.objects.filter(tags = pk)
        return context