from django.urls import path

from TODO_list.views import TagListView

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tags_list"),
]

app_name = "task_manager"
