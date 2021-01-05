from django.urls import path
from . import views


app_name = 'academy'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('schedule/', views.schedule, name='schedule'),
    path('enroll/', views.enroll, name='enroll'),
    path('classes/', views.classes, name='classes')
]
