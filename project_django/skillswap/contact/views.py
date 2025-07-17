from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ContactForm
from skill.models import Skill

@login_required
def contact_form(request, pk, skill_id):
    receiver = get_object_or_404(User, pk=pk)
    skill = get_object_or_404(Skill, id=skill_id)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.sender = request.user.username
            contact.email=request.user.email
            contact.receiver = receiver.email
            contact.save()
            return redirect('thank_you', skill_id=skill_id)
    else:
        form = ContactForm(initial={
            'sender':request.user.username,
            'email':request.user.email,
            'receiver':receiver.email

        })

    return render(request, 'messaging/contact_form.html', {'form': form, 'receiver': receiver, 'skill': skill})

def thank_you(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    return render(request, 'messaging/thank_you.html', {'skill': skill})



