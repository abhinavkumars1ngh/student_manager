from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if 'signup' in request.POST:
            User.objects.create_user(username=username, password=password)
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')