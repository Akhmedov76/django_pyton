from django.db import models


class Student(models.Model):
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    email = models.EmailField()
    student_id = models.IntegerField(max_length=50, unique=True)
    enrolled_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_start_date = models.DateField()

    def __str__(self):
        return self.course_name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField(max_length=2)

