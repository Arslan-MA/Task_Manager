from django.shortcuts import render, redirect
from app.models import Task


def all_tasks(request):
    context = {'tasks': Task.objects.all()}

    return render(request, 'allTasks.html', context)


def task_completed(request, task_id):
    if request.method == "GET":
        task = Task.objects.get(id=task_id)
        task.status = 'Выполнено'
        task.save()

        return redirect('home')


def create_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        date_of_creation = request.POST.get('date_of_creation')
        deadline_date = request.POST.get('deadline_date')
        priority_level = request.POST.get('priority_level')
        status = request.POST.get('status')

        Task.objects.create(name=name,
                            description=description,
                            date_of_creation=date_of_creation,
                            deadline_date=deadline_date,
                            priority_level=priority_level,
                            status=status)

        return redirect('home')

    return render(request, 'createTask.html')


def task_editing(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}

    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        date_of_creation = request.POST.get('date_of_creation')
        deadline_date = request.POST.get('deadline_date')
        priority_level = request.POST.get('priority_level')
        status = request.POST.get('status')

        task.name = name
        task.description = description
        task.date_of_creation = date_of_creation
        task.deadline_date = deadline_date
        task.priority_level = priority_level
        task.status = status
        task.save()

        return redirect('home')

    return render(request, 'taskEditing.html', context)
