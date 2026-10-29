from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render

from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def register(request):
    return render(request,'register.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        print(request.POST)

        preUser=User.objects.filter(username=username)
        if preUser:
            messages.success(request, 'Username already exists')
            return render(request, 'register.html')

        if pass1 != pass2:
            messages.error(request,'Passwords do not match')
            return render(request,'signup.html')
        print("password match")
        user = User.objects.create_user(username=username,password=pass1)
        user.save()
        login(request, user)
        messages.success(request,'User created successfully')
        return render(request,'home.html')

    return render(request,'signup.html')


