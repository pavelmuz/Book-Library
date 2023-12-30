from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CreateUserForm

# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('books')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("Username doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('books')
        else:
            print('Username OR password is incorrect')

    context = {'page': 'login'}

    return render(request, 'users/login-register.html', context)


def logout_user(request):
    logout(request)
    return redirect('books')


def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('books')
        print('An error during registration')

    context = {
        'page': 'register',
        'form': form
    }
    return render(request, 'users/login-register.html', context)
