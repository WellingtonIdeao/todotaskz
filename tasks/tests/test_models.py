from django.test import TestCase
from django.utils.text import slugify
from ..models import Category, Task


class CategoryModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        name = 'FOO text'
        Category.objects.create(name=name)

    def test_name_label(self):
        category = Category.objects.get(pk=1)
        field_name = category._meta.get_field('name').verbose_name
        self.assertEqual(field_name, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    def test_name_is_blank_false(self):
        category = Category.objects.get(pk=1)
        is_blank = category._meta.get_field('name').blank
        self.assertEqual(is_blank, False)

    def test_name_is_null_false(self):
        category = Category.objects.get(pk=1)
        is_null = category._meta.get_field('name').null
        self.assertEqual(is_null, False)

    def test_name_is_unique(self):
        category = Category.objects.get(pk=1)
        is_unique = category._meta.get_field('name').unique
        self.assertEqual(is_unique, True)

    def test_created_label(self):
        category = Category.objects.get(pk=1)
        field_name = category._meta.get_field('created').verbose_name
        self.assertEqual(field_name, 'created')

    def test_created_is_auto_now_add(self):
        category = Category.objects.get(pk=1)
        is_auto_now_add = category._meta.get_field('created').auto_now_add
        self.assertEqual(is_auto_now_add, True)

    def test_created_is_auto_now_false(self):
        category = Category.objects.get(pk=1)
        is_auto_now = category._meta.get_field('created').auto_now
        self.assertEqual(is_auto_now, False)

    def test_created_is_blank(self):
        category = Category.objects.get(pk=1)
        is_blank = category._meta.get_field('created').blank
        self.assertEqual(is_blank, True)

    def test_created_is_editable(self):
        category = Category.objects.get(pk=1)
        is_editable = category._meta.get_field('created').editable
        self.assertEqual(is_editable, False)

    def test_updated_label(self):
        category = Category.objects.get(pk=1)
        field_name = category._meta.get_field('updated').verbose_name
        self.assertEqual(field_name, 'updated')

    def test_updated_is_auto_now(self):
        category = Category.objects.get(pk=1)
        is_auto_now = category._meta.get_field('updated').auto_now
        self.assertEqual(is_auto_now, True)

    def test_updated_is_auto_now_add_false(self):
        category = Category.objects.get(pk=1)
        is_auto_now_add = category._meta.get_field('updated').auto_now_add
        self.assertEqual(is_auto_now_add, False)

    def test_updated_is_blank(self):
        category = Category.objects.get(pk=1)
        is_blank = category._meta.get_field('updated').blank
        self.assertEqual(is_blank, True)

    def test_updated_is_editable_false(self):
        category = Category.objects.get(pk=1)
        is_editable = category._meta.get_field('updated').editable
        self.assertEqual(is_editable, False)

    def test_get_absolute_url(self):
        category = Category.objects.get(pk=1)
        url = category.get_absolute_url()
        expected_url = '/tasks/category/1/'
        self.assertEqual(url, expected_url)

    def test_category_ordering(self):
        category = Category.objects.get(pk=1)
        ordering = category._meta.ordering
        self.assertEqual(ordering[0], 'created')

    def test_category_verbose_name_plural(self):
        category = Category.objects.get(pk=1)
        verbose_name_plural = category._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Categories')

    def test_object_name_is_name(self):
        category = Category.objects.get(pk=1)
        expected_object_name = category.name
        self.assertEqual(str(category), expected_object_name)


class TaskModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        name = 'FOO text'
        category = Category.objects.create(name=name)
        Task.objects.create(name=name,
                            slug=slugify(name),
                            category=category
                            )

    def test_name_label(self):
        task = Task.objects.get(pk=1)
        field_name = task._meta.get_field('name').verbose_name
        self.assertEqual(field_name, 'name')

    def test_name_max_length(self):
        task = Task.objects.get(pk=1)
        max_length = task._meta.get_field('name').max_length
        self.assertEqual(max_length, 500)

    def test_name_is_blank_false(self):
        task = Task.objects.get(pk=1)
        is_blank = task._meta.get_field('name').blank
        self.assertEqual(is_blank, False)

    def test_name_is_null_false(self):
        task = Task.objects.get(pk=1)
        is_null = task._meta.get_field('name').null
        self.assertEqual(is_null, False)

    def test_slug_label(self):
        task = Task.objects.get(pk=1)
        field_name = task._meta.get_field('slug').verbose_name
        self.assertEqual(field_name, 'slug')

    def test_slug_max_length(self):
        task = Task.objects.get(pk=1)
        max_length = task._meta.get_field('slug').max_length
        self.assertEqual(max_length, 50)

    def test_slug_is_blank_false(self):
        task = Task.objects.get(pk=1)
        is_blank = task._meta.get_field('slug').blank
        self.assertEqual(is_blank, False)

    def test_slug_is_null_false(self):
        task = Task.objects.get(pk=1)
        is_null = task._meta.get_field('slug').null
        self.assertEqual(is_null, False)

    def test_slug_is_unique(self):
        task = Task.objects.get(pk=1)
        is_unique = task._meta.get_field('slug').unique
        self.assertEqual(is_unique, True)

    def test_description_label(self):
        task = Task.objects.get(pk=1)
        field_name = task._meta.get_field('description').verbose_name
        self.assertEqual(field_name, 'description')

    def test_description_is_blank(self):
        task = Task.objects.get(pk=1)
        is_blank = task._meta.get_field('description').blank
        self.assertEqual(is_blank, True)

    def test_description_is_null_false(self):
        task = Task.objects.get(pk=1)
        is_null = task._meta.get_field('description').null
        self.assertEqual(is_null, False)

    def test_created_label(self):
        task = Task.objects.get(pk=1)
        field_name = task._meta.get_field('created').verbose_name
        self.assertEqual(field_name, 'created')

    def test_created_is_auto_now_add(self):
        task = Task.objects.get(pk=1)
        is_auto_now_add = task._meta.get_field('created').auto_now_add
        self.assertEqual(is_auto_now_add, True)

    def test_created_is_auto_now_false(self):
        task = Task.objects.get(pk=1)
        is_auto_now = task._meta.get_field('created').auto_now
        self.assertEqual(is_auto_now, False)

    def test_created_is_blank(self):
        task = Task.objects.get(pk=1)
        is_blank = task._meta.get_field('created').blank
        self.assertEqual(is_blank, True)

    def test_created_is_editable_false(self):
        task = Task.objects.get(pk=1)
        is_editable = task._meta.get_field('created').editable
        self.assertEqual(is_editable, False)

    def test_updated_label(self):
        task = Task.objects.get(pk=1)
        field_name = task._meta.get_field('updated').verbose_name
        self.assertEqual(field_name, 'updated')

    def test_updated_is_auto_now(self):
        task = Task.objects.get(pk=1)
        is_auto_now = task._meta.get_field('updated').auto_now
        self.assertEqual(is_auto_now, True)

    def test_updated_is_auto_now_add_false(self):
        task = Task.objects.get(pk=1)
        is_auto_now_add = task._meta.get_field('updated').auto_now_add
        self.assertEqual(is_auto_now_add, False)

    def test_updated_is_blank(self):
        task = Task.objects.get(pk=1)
        is_blank = task._meta.get_field('updated').blank
        self.assertEqual(is_blank, True)

    def test_updated_is_editable_false(self):
        task = Task.objects.get(pk=1)
        is_editable = task._meta.get_field('updated').editable
        self.assertEqual(is_editable, False)

    def test_expire_date_label(self):
        task = Task.objects.get(pk=1)
        field_name = task._meta.get_field('expire_date').verbose_name
        self.assertEqual(field_name, 'expire date')

    def test_expire_date_is_auto_now_add_false(self):
        task = Task.objects.get(pk=1)
        is_auto_now_add = task._meta.get_field('expire_date').auto_now_add
        self.assertEqual(is_auto_now_add, False)

    def test_expire_date_is_auto_now_false(self):
        task = Task.objects.get(pk=1)
        is_auto_now = task._meta.get_field('expire_date').auto_now
        self.assertEqual(is_auto_now, False)

    def test_expire_date_is_blank_false(self):
        task = Task.objects.get(pk=1)
        is_blank = task._meta.get_field('expire_date').blank
        self.assertEqual(is_blank, False)

    def test_task_ordering(self):
        task = Task.objects.get(pk=1)
        ordering = task._meta.ordering
        self.assertEqual(ordering[0], 'created')

    def test_get_absolute_url(self):
        task = Task.objects.get(pk=1)
        url = task.get_absolute_url()
        expect_url = '/tasks/task/1/'
        self.assertEqual(url, expect_url)

    def test_object_name_is_name(self):
        task = Task.objects.get(pk=1)
        expected_object_name = task.name
        self.assertEqual(str(task), expected_object_name)

    def test_category_related_name(self):
        related_name = Category._meta.get_field('task').related_name
        self.assertEqual(related_name, 'category_tasks')

    def test_category_related_query_name(self):
        related_query_name = Category._meta.get_field('task').related_query_name
        self.assertEqual(related_query_name, 'task')



