from django import forms
from .models import Category, Task


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name', 'description',
            'category', 'expire_date', 'is_done'
        ]