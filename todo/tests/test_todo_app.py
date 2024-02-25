from django.test import TestCase
from django.urls import reverse
from todo.models import Tag, Task
from todo.forms import TaskForm
from django.utils import timezone


class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(content="Test Task", is_done=False)
        self.assertEqual(task.__str__(), "Test Task")
        self.assertFalse(task.is_done)


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(tag.__str__(), "Test Tag")


class TaskFormTest(TestCase):
    def test_task_form_valid_data(self):
        tag = Tag.objects.create(name="Test Tag")
        form_data = {
            'content': 'Test Task',
            'deadline': timezone.now(),
            'is_done': False,
            'tags': [tag.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_data(self):
        form_data = {
            'content': '',
            'deadline': timezone.now(),
            'is_done': False,
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())


class TaskListViewTest(TestCase):
    def test_task_list_view_status_code(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)

    def test_task_list_view_uses_correct_template(self):
        response = self.client.get(reverse('task-list'))
        self.assertTemplateUsed(response, 'todo/task_list.html')


class TaskToggleDoneViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task", is_done=False)
        self.task.tags.set([self.tag])

    def test_toggle_done_view_redirects_correctly(self):
        response = self.client.post(
            reverse('toggle-task-done', args=[self.task.id]))
        self.assertRedirects(response, reverse('task-list'))

    def test_toggle_done_view_toggles_task_done_status(self):
        initial_status = self.task.is_done
        self.client.post(reverse('toggle-task-done', args=[self.task.id]))
        updated_task = Task.objects.get(id=self.task.id)
        self.assertNotEqual(initial_status, updated_task.is_done)

    def test_toggle_done_view_updates_task_correctly(self):
        initial_status = self.task.is_done
        self.client.post(reverse('toggle-task-done', args=[self.task.id]))
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.is_done, not initial_status)
