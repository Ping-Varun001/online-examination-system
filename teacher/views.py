from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from exam import models as QMODEL
from student import models as SMODEL
from exam import forms as QFORM



#for showing signup/login button for teacher
def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'teacher/teacherclick.html')

def teacher_signup_view(request):
    userForm=forms.TeacherUserForm()
    teacherForm=forms.TeacherForm()
    mydict={'userForm':userForm,'teacherForm':teacherForm}
    if request.method=='POST':
        userForm=forms.TeacherUserForm(request.POST)
        teacherForm=forms.TeacherForm(request.POST,request.FILES)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacher=teacherForm.save(commit=False)
            teacher.user=user
            teacher.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('teacherlogin')
    return render(request,'teacher/teachersignup.html',context=mydict)



def is_teacher(user):
    # allow superuser (admin)
    if user.is_superuser:
        return True
    return user.groups.filter(name='TEACHER').exists()

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'total_student':SMODEL.Student.objects.all().count()

    }
    return render(request,'teacher/teacher_dashboard.html',context=dict)

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_exam_view(request):
    return render(request,'teacher/teacher_exam.html')


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_exam_view(request):
    courseForm=QFORM.CourseForm()
    if request.method=='POST':
        courseForm=QFORM.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-exam')
    return render(request,'teacher/teacher_add_exam.html',{'courseForm':courseForm})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_exam.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def delete_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher/teacher-view-exam')

@login_required(login_url='adminlogin')
def teacher_question_view(request):
    return render(request,'teacher/teacher_question.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_question_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    existing_count = QMODEL.Question.objects.filter(course=course).count()

    QuestionFormSet = QFORM.QuestionFormSet

    if request.method == 'POST':
        formset = QuestionFormSet(
            request.POST,
            prefix='form'
        )

        if formset.is_valid():
            questions = formset.save(commit=False)
            for q in questions:
                q.course = course
                q.save()
            return HttpResponseRedirect('/teacher/teacher-view-question')
        else:
            print(formset.errors)

    else:
        formset = QuestionFormSet(
            queryset=QMODEL.Question.objects.none(),
            prefix='form'
        )

    return render(
        request,
        'teacher/teacher_add_question.html',
        {
            'formset': formset,
            'courses': course,
            'start_index': existing_count
        }
    )

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_question_view_list(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_add_question_list.html',{'courses':courses})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_question_view(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_question.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_question_view(request,pk):
    questions=QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request,'teacher/see_question.html',{'questions':questions})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_question_view(request,pk):
    question=QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')

from exam.models import Result
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from exam.models import Question, Result
from teacher.models import Teacher  

from exam.models import Course, Result

@login_required(login_url='teacherlogin')
def teacher_view_results(request):
    courses = Course.objects.all()

    course_data = []
    for c in courses:
        attempted = Result.objects.filter(exam=c).count()
        course_data.append({
            'course': c,
            'attempted': attempted
        })

    return render(
        request,
        'teacher/teacher_view_results.html',
        {'course_data': course_data}
    )

@login_required(login_url='teacherlogin')
def teacher_view_subject_results(request, pk):
    course = get_object_or_404(Course, id=pk)
    results = Result.objects.filter(exam=course)

    return render(
        request,
        'teacher/teacher_view_subject_results.html',
        {
            'course': course,
            'results': results
        }
    )

from django.contrib.auth import authenticate, login
from .forms import TeacherLoginForm

def teacherlogin_view(request):
    form = TeacherLoginForm()

    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)

                # 🔐 SUPERUSER → ADMIN DASHBOARD
                if user.is_superuser:
                    return redirect('admin-dashboard')

                # 👨‍🏫 TEACHER
                if user.groups.filter(name='TEACHER').exists():
                    return redirect('teacher-dashboard')

                return render(request, 'teacher/teacherlogin.html', {
                    'form': form,
                    'error': 'Not authorized'
                })

        return render(request, 'teacher/teacherlogin.html', {
            'form': form,
            'error': 'Invalid username or password'
        })

    return render(request, 'teacher/teacherlogin.html', {'form': form})