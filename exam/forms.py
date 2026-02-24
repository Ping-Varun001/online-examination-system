from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import AuthenticationForm
from django.forms import modelformset_factory
from . import models
from .models import Question

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)

    Email = forms.EmailField()

    Phone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message='Enter a valid 10-digit mobile number'
            )
        ]
    )

    Institute = forms.CharField(max_length=100)

    Message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 30})
    )

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        if not re.match(r'^[\w\.-]+@[\w-]+\.(com|in|org|edu)$', email):
            raise ValidationError("Enter a valid email address")
        return email


class TeacherSalaryForm(forms.Form):
    salary = forms.IntegerField()


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['course_name', 'question_number', 'total_marks']


class QuestionForm(forms.ModelForm):
    courseID = forms.ModelChoiceField(
        queryset=models.Course.objects.all(),
        empty_label="Course Name",
        to_field_name="id"
    )

    class Meta:
        model = models.Question
        fields = ['marks', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }


QuestionFormSet = modelformset_factory(
    Question,
    fields=['marks','question','option1','option2','option3','option4','answer'],
    extra=1
)


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )