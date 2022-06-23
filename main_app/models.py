from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=10000)
    tags = models.ManyToManyField(Tag, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']