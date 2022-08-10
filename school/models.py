from django.db import models


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=32, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    name = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
