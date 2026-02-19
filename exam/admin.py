from django.contrib import admin
from .models import Question,Result,Student,Course,Teacher,VideoCourse
# Register your models here.
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(VideoCourse)