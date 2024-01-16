from django.test import TestCase

from TODO_list.models import Tag, Task


class TagModelTest(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="work")
        self.assertEqual(str(tag), tag.name)

    def test_tag_ordering(self):
        position_1 = Tag.objects.create(name="work")
        position_2 = Tag.objects.create(name="shopping")
        expected_list = [position_2, position_1]
        actual_list = list(Tag.objects.all())
        self.assertEqual(actual_list, expected_list)


class TaskModelTest(TestCase):
    def test_task_str(self):
        task = Task.objects.create(
            content="Buy bread",
            is_completed=True
        )
        self.assertEqual(str(task), task.content)

    def test_task_ordering(self):
        task_1 = Task.objects.create(
            content="Buy bread",
            is_completed=True
        )
        task_2 = Task.objects.create(content="Update CV")
        expected_list = [task_2, task_1]
        actual_list = list(Task.objects.all())
        self.assertEqual(actual_list, expected_list)
