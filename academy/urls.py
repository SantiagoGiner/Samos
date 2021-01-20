from django.urls import path
from . import views
from .models import *


app_name = 'academy'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('schedule/', views.schedule, name='schedule'),
    path('enroll/', views.enroll, name='enroll'),
    path('classes/', views.classes, name='classes'),
    path('view_class/<str:class_type>/<int:class_id>', views.view_class, name='view_class'),
    path('profile/', views.profile, name='profile')
]
