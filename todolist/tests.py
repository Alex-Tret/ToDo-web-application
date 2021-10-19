import datetime
from unittest import mock

import pytz
from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import TodoList, Project

TEST_DATE = datetime.datetime(2022, 10, 19, 12, 00, tzinfo=pytz.utc)
TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)

class TestToDoApp(TestCase):
    """Class for CustomUser Model test"""

    def setUp(self):
        print("setup test started")
        """ Create a user object to be used by the tests """
        time_mock = datetime.datetime(2021, 10, 19, 12, 00, tzinfo=pytz.utc)

        with mock.patch('django.utils.timezone.now') as mock_time:
            mock_time.return_value = time_mock

            self.project = Project.objects.create(
                id=101,
                name='A good project',
            )

            self.todo = TodoList.objects.create(
                id=111,
                title="task 1 1",
                content ="some content sample",
                due_date = TEST_DATE,
                project = self.project,
            )

            def test_string_representation_project(self):
                print("str test started")
                proj = Project(name='Sample project')
                self.assertEqual(str(proj), proj.title)

            def test_string_representation_todo(self):
                todo = TodoList(title='A sample title',
                                content="sample content",
                                due_date=TEST_DATE,
                                project='A good project')
                self.assertEqual(str(todo), todo.title)

            def test_todo_content(self):
                self.assertEqual(f'{self.todo.title}', 'task 1 1')
                self.assertEqual(f'{self.todo.content}', 'some content sample')
                self.assertEqual(f'{self.todo.due_date}', TEST_DATE)
                self.assertEqual(f'{self.todo.project}', 'A good project')

            # def test_post_create_view(self):  # new
            #     response = self.client.post(reverse('post_new'), {
            #         'title': 'New title',
            #         'body': 'New text',
            #         'author': self.user,
            #     })
            #     self.assertEqual(response.status_code, 200)
            #     self.assertContains(response, 'New title')
            #     self.assertContains(response, 'New text')
            #
            # def test_post_update_view(self):  # новое
            #     response = self.client.post(reverse('post_edit', args='1'), {
            #         'title': 'Updated title',
            #         'body': 'Updated text',
            #     })
            #     self.assertEqual(response.status_code, 302)
            #
            # def test_post_delete_view(self):  # новое
            #     response = self.client.post(
            #         reverse('post_delete', args='1'))
            #     self.assertEqual(response.status_code, 302)


