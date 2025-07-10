from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm,RegistrationForm,LoginForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'user_auth/index.html')

def user_signup(request):
    if request.method == 'POST':
    
        user_form = UserForm(request.POST)
        profile_form = RegistrationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
       
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password']) 
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                messages.error(request, "Invalid login details.")
                return render(request, 'user_auth/login.html')
        else:
                user_form = UserForm()
                profile_form = RegistrationForm()
    else:
        form = RegistrationForm()
    return render(request, 'user_auth/register.html', {'form': form})



def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
               login(request,user)
               return redirect('index')
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed")
            print('username:{} and password {}'.format(username,password))
            return HttpResponse("Invalid login details")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def User_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


@login_required
def user_profile(request):
    return render(request,'user_auth/profile.html')