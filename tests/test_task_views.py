from django.test import TestCase
from django.urls import reverse

from TODO_list.models import Task

TASK_LIST_VIEW = "/"
TASK_CREATE_VIEW = "/tasks/create/"
TASK_UPDATE_VIEW = "/tasks/1/update/"
TASK_DELETE_VIEW = "/tasks/1/delete/"
TASK_STATUS_TOGGLE_VIEW = "/tasks/2/status-toggle/"


class TaskViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            content="Buy bread",
            is_completed=True
        )
        Task.objects.create(content="Update CV")

    # Test if all the pages are accessible
    def test_retrieve_task_list(self):
        response = self.client.get(TASK_LIST_VIEW)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_create_page(self):
        response = self.client.get(TASK_CREATE_VIEW)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_update_page(self):
        response = self.client.get(TASK_UPDATE_VIEW)
        task = Task.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["task"], task)

    def test_retrieve_task_delete_page(self):
        response = self.client.get(TASK_DELETE_VIEW)
        task = Task.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["task"], task)

    # Test if all the pages are accessible by their name
    def test_retrieve_task_list_by_name(self):
        response = self.client.get(reverse("todo_list:task_list"))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_create_page_by_name(self):
        response = self.client.get(reverse("todo_list:task_create"))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_update_page_by_name(self):
        response = self.client.get(reverse("todo_list:task_update", args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_delete_page_by_name(self):
        response = self.client.get(reverse("todo_list:task_delete", args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_task_status_toggle(self):
        # Test completing task
        self.assertFalse(Task.objects.get(id=2).is_completed)
        self.client.get(TASK_STATUS_TOGGLE_VIEW)
        self.assertTrue(Task.objects.get(id=2).is_completed)

        # Test undo completing task
        self.client.get(TASK_STATUS_TOGGLE_VIEW)
        self.assertFalse(Task.objects.get(id=2).is_completed)
