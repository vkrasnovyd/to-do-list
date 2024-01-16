from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from TODO_list.forms import TagForm, TaskForm
from TODO_list.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "base_form.html"
    success_url = reverse_lazy("todo_list:tag_list")

    def get_context_data(self, **kwargs):
        context = super(TagCreateView, self).get_context_data()
        context["form_object_name"] = "tag"
        return context


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "base_form.html"
    success_url = reverse_lazy("todo_list:tag_list")

    def get_context_data(self, **kwargs):
        context = super(TagUpdateView, self).get_context_data()
        context["form_object_name"] = "tag"
        return context


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag_list")

    def get_context_data(self, **kwargs):
        context = super(TagDeleteView, self).get_context_data()
        context["object_name"] = "tag"
        return context


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "base_form.html"
    success_url = reverse_lazy("todo_list:task_list")

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data()
        context["form_object_name"] = "task"
        return context


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "base_form.html"
    success_url = reverse_lazy("todo_list:task_list")

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data()
        context["form_object_name"] = "task"
        return context


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("todo_list:task_list")

    def get_context_data(self, **kwargs):
        context = super(TaskDeleteView, self).get_context_data()
        context["object_name"] = "task"
        return context


class TaskStatusToggleView(views.View):
    @staticmethod
    def get(request, pk):
        task = get_object_or_404(Task, id=pk)
        task.is_completed = not task.is_completed
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_list:task_list"))
