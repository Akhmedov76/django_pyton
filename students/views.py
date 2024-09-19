from django.shortcuts import render
from .models import Student
from django.views.generic import TemplateView


class StudentListView(TemplateView):
    template_name = "students/student.html"

