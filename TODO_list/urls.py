from django.urls import path

from TODO_list.views import (
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskListView,
)

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tags/create/", TagCreateView.as_view(), name="tags_create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tags_update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tags_delete"),
    path("", TaskListView.as_view(), name="tasks_list"),
]

app_name = "todo_list"
