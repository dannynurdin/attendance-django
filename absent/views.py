from django.shortcuts import render
from .forms import TeacherForm 
  
# Create your views here. 
def teacher_view(request):
    context ={} 
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()

    
    context['form']= TeacherForm() 
    return render(request, "home.html", context)

