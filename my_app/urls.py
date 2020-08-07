from django.urls import path
from my_app import views


urlpatterns = [
    path('teacher',views.TeacherListView.as_view(), name='teacher_list'),
    path('student',views.StudentListView.as_view(), name='student_list'),
    path('teacher-form',views.TeacherCreateView.as_view(), name='teacher_form'),
    path('student-form',views.StudentCreateView.as_view(), name='student_form'),
    path('teacher-form-update/<int:id>',views.TeacherUpdateView.as_view(), name='teacher_form_update'),
    path('teacher-delete/<int:id>',views.TeacherDeleteView.as_view(), name='teacher_delete'),
    path('student-form-update/<int:id>',views.StudentUpdateView.as_view(), name='student_form_update'),
    path('student-delete/<int:id>',views.StudentDeleteView.as_view(), name='student_delete'),
    path('student-detail/<int:id>',views.StudentDetailView.as_view(), name='student_detail'),
    path('', views.AboutView.as_view(), name='about')
]