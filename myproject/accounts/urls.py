from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('',views.home , name='home'),
    path('products/', views.products , name='products'),
    path('register/', views.register , name='register'),
    path('signup/', views.user_register , name='signup'),
    path('login/', views.user_login , name='login'),

]
