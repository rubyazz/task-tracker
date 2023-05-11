from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/change-status/', views.change_status, name='change_status'),
    path('create/', views.create_task, name='create'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete'),

]