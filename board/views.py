from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html', {'projects': projects, 'skills': skills})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})