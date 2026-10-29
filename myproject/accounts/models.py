from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    province_bron  = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    # joined_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(help_text='Enter your bio', blank=True )

class StudentCourse(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    summary = models.TextField(help_text='Enter your summary', blank=True )
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    reading_time = models.CharField(max_length=3)
    link = models.PositiveIntegerField(default=0)
    director = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='posts')

class Comment(models.Model):
    post = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

class Post_Image(models.Model):
    post = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)

class Saved_Post(models.Model):
    post = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

