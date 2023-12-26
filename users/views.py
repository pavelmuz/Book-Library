from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

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

        print('Username OR password is incorrect')

    context = {'page': 'login'}

    return render(request, 'users/login-register.html', context)
