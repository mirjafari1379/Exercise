from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('',views.home),
    path('products/', views.products),
    path('register/', views.register),
    path('signup/', views.user_register , name='signup'),
]
