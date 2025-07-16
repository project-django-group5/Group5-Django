from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm,RegistrationForm,LoginForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from skill.models import Skill
from review.models import Review

# def index(request):
#     return render(request,'user_auth/index.html')

def user_signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = RegistrationForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password']) 
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')  

        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserForm()
        profile_form = RegistrationForm()

    return render(request, 'user_auth/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




def User_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    
    return render(request, 'user_auth/login.html', {'form': form})


@login_required
def User_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


@login_required
def user_profile(request):
    user = request.user
    skills = Skill.objects.filter(user=user).annotate(
        average_rating=Avg('review__rating'),  
        review_count=Count('review')
    )

    return render(request, 'user_auth/profile.html', {
        'user_profile': user,
        'skills': skills,
    })

@login_required
def edit_profile(request):
    user_detail, created = UserDetail.objects.get_or_create(user= request.user)

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES, instance=user_detail)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm(instance=user_detail)

    return render(request, 'user_auth/edit_profile.html', {'detail_form': form})