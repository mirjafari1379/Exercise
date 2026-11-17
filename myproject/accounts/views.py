from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        context = {'user': user}
        return render(request, 'index.html', context)
    return render(request, 'register.html')

def products(request):
    return render(request, 'products.html')

def register(request):
    return render(request, 'register.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        print(request.POST)

        preUser = User.objects.filter(username=username)
        if preUser:
            messages.success(request, 'Username already exists')
            return render(request, 'singup.html')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')
        print("password match")
        user = User.objects.create_user(username=username, password=pass1)
        user.save()
        login(request, user)
        messages.success(request, 'User created successfully')
        return render(request, 'index.html')

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید')
            return redirect('/')

        messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
        return render(request, 'register.html')

    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('accounts:home')
