from django import forms
from .models import Teacher, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','subject']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll','year','mail','phone','course']