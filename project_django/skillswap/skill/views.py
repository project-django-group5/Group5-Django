from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Exists, OuterRef
from review.models import Review

@login_required
def skill_list(request):
    skill= Skill.objects.annotate(
        average_rating=Avg('review__rating'),
        review_count=Count('review')
    )
    if request.user.is_authenticated:
        skill = skill.annotate(
            has_reviewed=Exists(
                Review.objects.filter(
                    reviewer=request.user,
                    skill=OuterRef('pk')
                )
            )
    )
    return render(request, 'skill/skill_list.html',{'skills': skill})

@login_required
def skill_add(request):
    if request.method =="POST":
        form= SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.user= request.user
            skill.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'skill/skill_add.html', {'form': form})
        

