from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('projects', views.Projects.as_view(), name="projects"),
    path('publications', views.Publications.as_view(), name="publications"),

    path('blog', views.Blog.as_view(), name="blog"),
    path('tags', views.TagList.as_view(), name="tag-list"),
    path('tag/<int:pk>', views.TaggedPosts.as_view(), name="tagged-posts"),
    path('post/<int:pk>', views.PostDetail.as_view(), name="postdetail"),
    path('post/<int:pk>/edit', views.PostUpdate.as_view(), name="post-update"),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name="postdelete"),
    path('post/new', views.PostCreate.as_view(), name="post-create"),
    path('tag/new', views.TagCreate.as_view(), name="tag-create"),
    path('tag/<int:pk>/rename', views.TagUpdate.as_view(), name="tag-update"),
    path('tag/<int:pk>/delete', views.TagDelete.as_view(), name="tag-delete")
]