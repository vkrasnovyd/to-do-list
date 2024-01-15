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
    success_url = reverse_lazy("todo_list:tags_list")

    def get_context_data(self, **kwargs):
        context = super(TagCreateView, self).get_context_data()
        context["form_object_name"] = "tag"
        return context


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "base_form.html"
    success_url = reverse_lazy("todo_list:tags_list")

    def get_context_data(self, **kwargs):
        context = super(TagUpdateView, self).get_context_data()
        context["form_object_name"] = "tag"
        return context


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("todo_list:tags_list")

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
    success_url = reverse_lazy("todo_list:tasks_list")

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data()
        context["form_object_name"] = "task"
        return context

