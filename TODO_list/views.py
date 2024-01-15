from django.urls import reverse_lazy
from django.views import generic

from TODO_list.forms import TagForm
from TODO_list.models import Tag


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
