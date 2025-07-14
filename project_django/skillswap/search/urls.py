from django.urls import path
from . import views

urlpatterns = [
    path('skill_search/',views.skill_search,name='skill_search'),
    path('skill_detail/',views.skill_detail,name='skill_detail'),
]
 
