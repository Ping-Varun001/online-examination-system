from django.urls import path
from teacher import views


urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('teacher-add-question/<int:pk>/', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-add-question_list', views.teacher_add_question_view_list,name='teacher-add-question_list'),
path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
path('teacher-view-results/',views.teacher_view_results,name='teacher_view_results'),
path('teacher-view-results/',views.teacher_view_results,name='teacher_view_results'),
path('teacher-view-results/<int:pk>/',views.teacher_view_subject_results,name='teacher_view_subject_results'),
path('teacherlogin', views.teacherlogin_view, name='teacherlogin'),

]