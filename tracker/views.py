from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = {
        'backlog': Task.objects.filter(status='backlog'),
        'doing': Task.objects.filter(status='doing'),
        'review': Task.objects.filter(status='review'),
        'done': Task.objects.filter(status='done'),
    }
    task_counts = {status: queryset.count() for status, queryset in tasks.items()}
    return render(request, 'task_list.html', {'tasks': tasks, 'task_counts': task_counts})


def change_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()
        return redirect('tracker:task_list')


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


def delete_task(request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('tracker:task_list')