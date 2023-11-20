from django.urls import path
from . import views


urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('<int:staf_id>', views.view_profesori, name='view_profesori'),
    path('add/', views.add, name='add'),
    path('edit/<int:staf_id>/', views.edit, name='edit'),
    path('delete/<int:staf_id>/', views.delete, name='delete'),
    path('website/', views.website, name='website'),
    path('<int:kurs_id>', views.view_website, name='view_website'),
    path('shtoLende/', views.shtoLende, name='shtoLende'),
    path('editLendet/<int:kurs_id>/', views.editLendet, name='editLendet'),
    path('deleteLendet/<int:kurs_id>/', views.deleteLendet, name='deleteLendet'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('subject/<int:subject_id>/', views.subject_details, name='subject_details'),
    path('shto/', views.shto, name='shto'),
    path('subject/<int:subject_id>/details', views.details, name='details'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('costum_dashboard/', views.custom_dashboard, name='custom_dashboard'),
    path('student/register/', views.register_student, name='register_student'),
    path('logout/', views.custom_logout, name='custom_logout'),

]
