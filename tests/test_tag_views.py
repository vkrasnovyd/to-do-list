from django.test import TestCase
from django.urls import reverse

from TODO_list.models import Tag

TAG_LIST_VIEW = "/"
TAG_CREATE_VIEW = "/tags/create/"
TAG_UPDATE_VIEW = "/tags/1/update/"
TAG_DELETE_VIEW = "/tags/1/delete/"


class TagViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="work")

    # Test if all the pages are accessible
    def test_retrieve_tag_list(self):
        response = self.client.get(TAG_LIST_VIEW)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_tag_create_page(self):
        response = self.client.get(TAG_CREATE_VIEW)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_tag_update_page(self):
        response = self.client.get(TAG_UPDATE_VIEW)
        tag = Tag.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"], tag)

    def test_retrieve_tag_delete_page(self):
        response = self.client.get(TAG_DELETE_VIEW)
        tag = Tag.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"], tag)

    # Test if all the pages are accessible by their name
    def test_retrieve_tag_list_by_name(self):
        response = self.client.get(reverse("todo_list:tag_list"))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_tag_create_page_by_name(self):
        response = self.client.get(reverse("todo_list:tag_create"))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_tag_update_page_by_name(self):
        response = self.client.get(reverse("todo_list:tag_update", args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_tag_delete_page_by_name(self):
        response = self.client.get(reverse("todo_list:tag_delete", args=[1]))
        self.assertEqual(response.status_code, 200)
