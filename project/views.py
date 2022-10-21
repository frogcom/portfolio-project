from django.shortcuts import render, redirect, get_object_or_404
from .models import Project

# Create your views here.

def home(request):
 project = Project.objects
 return render(request, 'project/project.html', {'project': project})

def detail(request, project_id):
 project = get_object_or_404(Project, pk=project_id)
 return render(request, 'project/detail.html', {'project': project})