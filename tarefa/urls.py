from django.urls import path
from .views import List, Create, Edit, Delete

urlpatterns = [
    path('', List, name = 'List'),
    path('create/', Create, name = 'Create'),
    path('edit/<int:id>', Edit, name = 'Edit'),
    path('delete/<int:id>', Delete, name = 'Delete'),
]