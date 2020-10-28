from django.urls import path
from .views import teacher_view, index_view, classes_view, student_view, record_view, absent_view

urlpatterns = [
    path('', index_view, name="index"),
    path('teacher/', teacher_view, name="teacher"),
    path('record/', record_view),
    path('classes/', classes_view),
    path('student/', student_view),
    path('absent/', absent_view)
]