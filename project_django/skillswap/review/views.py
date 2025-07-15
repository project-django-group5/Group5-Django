from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.models import User
from django.contrib import messages
from skill.models import Skill

# Create your views here.


def leave_review(request, pk, skill_id):

    receiver = get_object_or_404(User, pk=pk)
    skill = get_object_or_404(Skill, pk=skill_id)

    if receiver == request.user:
        messages.error(request, "You cannot review yourself.")
        return redirect('skill_detail', pk=skill.id)

    existing_review = Review.objects.filter(reviewer=request.user,
                                            receiver=receiver,
                                            skill=skill
                                            ).first()
    if existing_review:
        messages.warning(request, "You have already reviewed this skill.")
        return redirect('skill_detail', pk=skill.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.receiver = receiver
            review.skill = skill
            review.save()
            messages.success(request, "Review submitted successfully.")
            return redirect('skill_detail', pk=skill.id)
    else:
        form = ReviewForm()

    return render(request, 'review/leave_review.html', {'form': form,
                                                        'skill': skill,
                                                        'receiver': receiver})
