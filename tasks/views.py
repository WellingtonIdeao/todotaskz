from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Task
from .forms import CategoryModelForm, TaskModelForm
from django.utils.text import slugify


class CategoryListView(ListView):
    model = Category
    template_name = 'tasks/category/list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'tasks/category/detail.html'
    context_object_name = 'category'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'tasks/category/registration/form.html'


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'tasks/category/registration/form.html'
    success_url = reverse_lazy('tasks:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'tasks/category/registration/check_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('tasks:category_list')


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task/list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task/detail.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'tasks/task/registration/form.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'tasks/task/registration/form.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task/registration/check_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:task_list')


'''def category_register(request):

    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.slug = slugify(new_form.name)
            new_form.save()
            return redirect(reverse('tasks:category_list'))
    else:
        form = CategoryModelForm()
    return render(request,
                  'tasks/category/registration/form.html',
                  {'form': form})
'''
