from django.urls import path
from .views import teacher_view

urlpatterns = [
    path('teacher/', teacher_view, name="teacher"),
]