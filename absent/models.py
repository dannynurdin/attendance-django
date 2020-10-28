from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Absent(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

