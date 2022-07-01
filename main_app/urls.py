from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('projects', views.Projects.as_view(), name="projects"),
    path('publications', views.Publications.as_view(), name="publications"),

    path('blog', views.Blog.as_view(), name="blog"),
    path('archives', views.Archives.as_view(), name="archives"),
    path('tag/<int:pk>', views.TaggedPosts.as_view(), name="tagged-posts"),
    path('post/<int:pk>', views.PostDetail.as_view(), name="postdetail"),
    path('post/<int:pk>/add-comment', views.AddComment.as_view(), name="add-comment"),
    path('<int:post>/<int:comment>/delete-comment', views.DeleteComment.as_view(), name="delete-comment"),

    path('accounts/signup', views.Signup.as_view(), name="signup"),
]