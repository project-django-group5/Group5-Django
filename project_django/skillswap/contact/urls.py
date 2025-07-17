from django.urls import path
from . import views

urlpatterns = [
    path('contact_form/<int:pk>/<int:skill_id>/', views.contact_form, name="contact_form"),
    path('thank_you/<int:skill_id>/', views.thank_you, name='thank_you'),
]
