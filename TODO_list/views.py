from django.views import generic

from TODO_list.models import Tag


class TagListView(generic.ListView):
    model = Tag
