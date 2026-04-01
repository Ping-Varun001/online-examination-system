from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Entry
    path('studentclick', views.studentclick_view, name='studentclick'),

    # Auth — FIXED: Added redirect URL directly to student dashboard
    path('studentlogin', views.student_login_view, name='studentlogin'),

    path('studentsignup', views.student_signup_view, name='studentsignup'),

    # Dashboard
    path('student-dashboard', views.student_dashboard_view, name='student-dashboard'),

    # Exam
    path('student-exam', views.student_exam_view, name='student-exam'),
    path('take-exam/<int:pk>', views.take_exam_view, name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam_view, name='start-exam'),

    # Results
    path('calculate-marks', views.calculate_marks_view, name='calculate-marks'),
    path('view-result', views.view_result_view, name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view, name='check-marks'),
    path('student-marks', views.student_marks_view, name='student-marks'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)