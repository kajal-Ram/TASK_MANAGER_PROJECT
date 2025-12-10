from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.admin = User.objects.create_superuser(username="admin", password="12345")
        Task.objects.create(title="User Task", owner=self.user)
        Task.objects.create(title="Admin Task", owner=self.admin)

    def test_task_owner(self):
        task = Task.objects.get(title="User Task")
        self.assertEqual(task.owner.username, "testuser")
