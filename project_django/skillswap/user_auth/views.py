
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import LoginForm,RegistrationForm
#from django.contrib.auth.models import UserAuthenticate
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'templates/register.html', {'form': form})

def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
               login(request,user)
               return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed")
            print('username:{} and password {}'.format(username,password))
            return HttpResponse("Invalid login details")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def User_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')