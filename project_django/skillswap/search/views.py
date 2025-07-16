from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from skill.models import Skill
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from review.models import Review 
from .forms import SkillSearchForm

def skill_search(request):
    skills = Skill.objects.all()

    categories = Skill.objects.values_list('category', flat=True).distinct()
    titles = Skill.objects.values_list('title', flat=True).distinct()
    locations = Skill.objects.values_list('location', flat=True).exclude(location='').distinct()
    availabilities = Skill.objects.values_list('availability', flat=True).distinct()

    dynamic_choices = {
        'categories': categories,
        'titles': titles,
        'locations': locations,
        'availabilities': availabilities,
    }

    form = SkillSearchForm(request.GET or None, dynamic_choices=dynamic_choices)

    if form.is_valid():
        cd = form.cleaned_data

        if cd.get('skill_type'):
            skills = skills.filter(skill_type=cd['skill_type'])

        if cd.get('category'):
            skills = skills.filter(category=cd['category'])

        if cd.get('title'):
            skills = skills.filter(title=cd['title'])

        if cd.get('location'):
            skills = skills.filter(location=cd['location'])

        if cd.get('availability'):
            skills = skills.filter(availability=cd['availability'])

    skills = skills.annotate(average_rating=Avg('review__rating'), review_count=Count('review'))

    context = {
        'skills': skills,
        'search_form': form,
    }
    return render(request, 'search/skill_search.html', context)



@login_required
def skill_detail(request, pk):
    skill = Skill.objects.annotate(
        average_rating=Avg('review__rating'),
        review_count=Count('review')
    ).get(pk=pk)

    reviews = Review.objects.filter(skill=skill).select_related('reviewer')

    has_reviewed = False
    if request.user.is_authenticated:
        has_reviewed = Review.objects.filter(
            reviewer=request.user,
            skill=skill
        ).exists()
    next_page = request.GET.get('next', 'skill_list')

    return render(request, 'search/skill_detail.html', {
        'skill': skill,
        'reviews': reviews,
        'has_reviewed': has_reviewed,
        'next_page': next_page
    })