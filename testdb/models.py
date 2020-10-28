from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Teacher Name")
    email = models.EmailField(max_length=50, verbose_name="Email")

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=50, verbose_name="Class Name")
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE, verbose_name="Teacher")

    def __str__(self):
        return self.name

class Absents(models.Model):
    name = models.CharField(max_length=100, verbose_name="Absent")
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name="Class")

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name="Class")
    email = models.EmailField(max_length=50, verbose_name="Email")
    image = models.ImageField(upload_to="student/")

    def __str__(self):
        return self.name

class Records(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="Student Name")
    absent = models.ForeignKey(Absents, on_delete=models.CASCADE, verbose_name="Absents")
    attendance = models.PositiveIntegerField()
    time = models.TimeField(auto_created=True)

    def __str__(self):
        return str(self.id)