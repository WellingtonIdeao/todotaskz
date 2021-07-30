from django.test import TestCase
from django.utils.text import slugify
from ..models import Category


class CategoryModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        name = 'FOO text'
        Category.objects.create(name=name, slug=slugify(name))

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

    def test_slug_max_length(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('slug').max_length
        self.assertEqual(max_length, 50)

    def test_slug_is_blank_false(self):
        category = Category.objects.get(pk=1)
        is_blank = category._meta.get_field('slug').blank
        self.assertEqual(is_blank, False)

    def test_slug_is_unique(self):
        category = Category.objects.get(pk=1)
        is_unique = category._meta.get_field('slug').unique
        self.assertEqual(is_unique, True)

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


