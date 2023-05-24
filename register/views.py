from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("home.html")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, "login.html")
    

def sign_up(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
    
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                print('username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=confirm_password, email=email)
                user.save();
                print('user created')
        else:
            print('password not matching...')
        return redirect('home.html')
            
    else:
        return render(request, "sign_up.html")


def logout(request):
        auth.logout(request)
        return redirect('home.html')

def wallet(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, email=email, password=password)
        
        if user.is_authenticated:
            return redirect("wallet.html")
        else:
            return redirect('sign_up.html')
    else:
        return render(request, "wallet.html")
    