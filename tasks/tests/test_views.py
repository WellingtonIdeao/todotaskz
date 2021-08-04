from django.test import TestCase
from django.urls import reverse
from ..models import Category, Task


class CategoryListViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 3 categories objects
        number_of_categories = 3
        for cat_id in range(number_of_categories):
            Category.objects.create(name='FOO text '+str(cat_id))

    def test_view_url_exists_at_desired_location(self):
        url = '/tasks/category/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/category/list.html'
        url = reverse('tasks:category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_name(self):
        url = reverse('tasks:category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('categories' in response.context)


class CategoryDetailViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='FOO text')

    def test_view_url_exists_at_desired_location(self):
        url = '/tasks/category/'
        response = self.client.get(url, kwargs={'pk': 1})
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:category_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_get_absolute_url(self):
        category = Category.objects.get(pk=1)
        url = category.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/category/detail.html'
        url = reverse('tasks:category_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_name(self):
        url = reverse('tasks:category_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('category' in response.context)


class CategoryCreateViewTests(TestCase):

    def test_view_url_exist_at_desired_location(self):
        url = '/tasks/category/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:category_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/category/registration/form.html'
        url = reverse('tasks:category_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)


class CategoryUpdateViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='FOO text')

    def test_view_url_exist_at_desired_location(self):
        url = '/tasks/category/1/edit/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:category_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/category/registration/form.html'
        url = reverse('tasks:category_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)


class CategoryDeleteViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='FOO text')

    def test_view_url_exist_at_desired_location(self):
        url = '/tasks/category/1/delete/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:category_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/category/registration/check_delete.html'
        url = reverse('tasks:category_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_success_url(self):
        url = reverse('tasks:category_delete', kwargs={'pk': 1})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)


class TaskListViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_tasks = 3
        category = Category.objects.create(name='FOO text')
        for task_id in range(number_of_tasks):
            Task.objects.create(name='FOO text',
                                category=category,
                                )

    def test_view_url_exists_at_desired_location(self):
        url = '/tasks/task/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/task/list.html'
        url = reverse('tasks:task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_name(self):
        url = reverse('tasks:task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('tasks' in response.context)


class TaskDetailViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='FOO text')
        Task.objects.create(name='FOO text',
                            category=category,
                            )

    def test_view_url_exists_at_desired_location(self):
        url = '/tasks/task/'
        response = self.client.get(url, kwargs={'pk': 1})
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:task_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_get_absolute_url(self):
        task = Task.objects.get(pk=1)
        url = task.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/task/detail.html'
        url = reverse('tasks:task_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_name(self):
        url = reverse('tasks:task_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('task' in response.context)


class TaskCreateViewTests(TestCase):

    def test_view_url_exist_at_desired_location(self):
        url = '/tasks/task/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:task_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/task/registration/form.html'
        url = reverse('tasks:task_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)


class TaskUpdateViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='FOO text')
        Task.objects.create(name='FOO text',
                            category=category,
                            )

    def test_view_url_exist_at_desired_location(self):
        url = '/tasks/task/1/edit/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:task_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/task/registration/form.html'
        url = reverse('tasks:task_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)


class TaskDeleteViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='FOO text')
        Task.objects.create(name='FOO text',
                            category=category,
                            )

    def test_view_url_exist_at_desired_location(self):
        url = '/tasks/task/1/delete/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('tasks:task_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        template_name = 'tasks/task/registration/check_delete.html'
        url = reverse('tasks:task_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_success_url(self):
        url = reverse('tasks:task_delete', kwargs={'pk': 1})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

