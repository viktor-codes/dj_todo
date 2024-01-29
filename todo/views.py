from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Task, Tag
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks,
    }

    return render(request, 'index.html', context)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task_list.html"

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', '-created_at')


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = "task-list"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = "task-list"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = "task-list"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tag_list.html"


class TagDetailView(generic.DetailView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = "tag-list"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = "tag-list"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = "tag-list"


def toggle_task_done(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    task.is_done = not task.is_done

    task.save()
    return redirect('task-list')
