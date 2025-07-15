from django.urls import path
from . import views

urlpatterns = [
    path('leave_review/', views.leave_review, name='leave_review'),
   
]
