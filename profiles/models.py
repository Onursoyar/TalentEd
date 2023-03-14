from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "DRAFT"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="profile_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='profile_likes', blank=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    approved = models.BooleanField(default=False)