from django.urls import path

from TODO_list.views import (
    TagListView,
    TagCreateView,
)

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tags/create/", TagCreateView.as_view(), name="tags_create"),
]

app_name = "todo_list"
