from django.contrib import admin
from .models import Post, Tag, Membership, Comment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Membership)