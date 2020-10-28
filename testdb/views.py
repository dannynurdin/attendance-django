from django.shortcuts import render
from .forms import TeacherForm, ClassesForm, AbsentsForm, RecordsForm, StudentsForm
def index_view(request):
    return render(request, "home.html")

def teacher_view(request):
    context ={} 
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
    context['form']= TeacherForm() 
    return render(request, "teacher.html", context)
    
def classes_view(request):
    context ={} 
    if request.method == 'POST':
        form = ClassesForm(request.POST)
        if form.is_valid():
            form.save()
    context['form']= ClassesForm() 
    return render(request, "classes.html", context)

def absent_view(request):
    context ={} 
    if request.method == 'POST':
        form = AbsentsForm(request.POST)
        if form.is_valid():
            form.save()
    context['form']= AbsentsForm() 
    return render(request, "absent.html", context)

def record_view(request):
    context ={} 
    if request.method == 'POST':
        form = RecordsForm(request.POST)
        if form.is_valid():
            form.save()
    context['form']= RecordsForm() 
    return render(request, "record.html", context)

def student_view(request):
    context ={} 
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
    context['form']= StudentsForm() 
    return render(request, "teacher.html", context)