from django.shortcuts import render
from .forms import TeacherForm
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