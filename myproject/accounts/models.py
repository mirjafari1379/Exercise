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



