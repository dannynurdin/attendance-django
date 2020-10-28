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

class ClassesForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'

class AbsentsForm(forms.ModelForm):
    class Meta:
        model = Absents
        fields = '__all__'

class RecordsForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = '__all__'

