from django.shortcuts import render
from django.views import generic
from .models import Instructor

# Create your views here.
class InstructorListView(generic.ListView):
    model = Instructor