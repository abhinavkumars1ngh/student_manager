from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from notes.models import Note

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    notes = Note.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'notes': notes
    })

@login_required
def add_task(request):
    Task.objects.create(
        user=request.user,
        title=request.POST['title']
    )
    return redirect('dashboard')

@login_required
def delete_task(request, id):
    Task.objects.get(id=id).delete()
    return redirect('dashboard')

@login_required
def toggle_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('dashboard')