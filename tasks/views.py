from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'tasks/category/list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'tasks/category/detail.html'
    context_object_name = 'category'


