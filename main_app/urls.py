from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('projects', views.Projects.as_view(), name="projects"),
    path('publications', views.Publications.as_view(), name="publications"),

    path('blog', views.Blog.as_view(), name="blog"),
    path('tag/<int:pk>', views.TaggedPosts.as_view(), name="tagged-posts"),
    path('post/<int:pk>', views.PostDetail.as_view(), name="postdetail"),
]