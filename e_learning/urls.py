"""
URL configuration for e_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from stafi import views
from stafi.views import CustomLoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('stafi/',include('stafi.urls')),
    path('', views.choose_login, name='choose_login'),
    path('stafi/custom_home', views.custom_home, name='custom_home'),
    path('stafi/login/', auth_views.LoginView.as_view(), name='login'),
    path('stafi/logout/', views.custom_logout, name='custom_logout'),
    path('stafi/register/', views.register_student, name='register_student'),
    path('login_student/', CustomLoginView.as_view(), name='login_student'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_student'),
    path('<int:subject_id>/pdfs/<str:leksioni>', views.serve_lesson_file, name='serve_lesson_file'),

]
