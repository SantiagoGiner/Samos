from django.conf import settings
from django.conf.urls.static import static
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
    path('courses/', views.courses, name='courses'),
    path('view_course/<int:course_id>/', views.view_course, name='view_course'),
    path('drop_course/<int:course_id>/', views.view_course, name='drop_course'),
    path('account/', views.account, name='account'),
    path('account/<str:action>/', views.account, name='change_account'),
    path('profile/<int:profile_id>/<str:action>/', views.change_profile, name='change_profile'),
    path('gallery/', views.gallery, name='gallery')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
