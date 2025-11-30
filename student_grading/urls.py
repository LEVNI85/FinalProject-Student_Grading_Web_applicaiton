from django.urls import path
from . import views

urlpatterns = [
    path("subjects/", views.subject_list, name="subject_list"),
    path("subjects/add/", views.subject_create, name="subject_create"),
    path("subjects/<int:pk>/edit/", views.subject_update, name="subject_update"),
    path("subjects/<int:pk>/delete/", views.subject_delete, name="subject_delete"),
    #--------------------------------------
    path("lecturers/", views.lecturer_list, name="lecturer_list"),
    path("students/", views.student_list, name="student_list"),
    path("students/<int:pk>/details/", views.student_detail, name="student_detail"),
    path("scores/<int:pk>/edit/", views.score_update, name="score_update"),
]