from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

# class StudentCourse(models.Model):
#     name = models.CharField(max_length=100)
#     level = models.CharField(max_length=100)
#     duration = models.CharField(max_length=100)
#     summary = models.TextField(help_text='Enter your summary', blank=True )
#     teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     reading_time = models.CharField(max_length=3)
#     link = models.PositiveIntegerField(default=0)
#     director = models.PositiveIntegerField(default=0)
#     image = models.ImageField(upload_to='posts')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

class Post_Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)

class Saved_Post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)