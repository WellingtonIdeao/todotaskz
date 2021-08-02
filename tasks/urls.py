from django.urls import path
from .views import CategoryListView, CategoryDetailView, TaskListView, TaskDetailView, \
    CategoryCreateView

app_name = 'tasks'

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('task/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),

]
