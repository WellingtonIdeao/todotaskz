from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('tasks:category_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,
                                 related_name='category_tasks',
                                 related_query_name='task',
                                 on_delete=models.CASCADE)
    expire_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('tasks:task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


