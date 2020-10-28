from django import forms
from .models import Teachers, Students, Classes, Absents, Records

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'