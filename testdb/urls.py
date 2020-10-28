from django.urls import path
from .views import teacher_view, index_view

urlpatterns = [
    path('', index_view, name="index"),
    path('teacher/', teacher_view, name="teacher"),
]