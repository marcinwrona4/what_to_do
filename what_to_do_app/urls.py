from django.urls import path

from . import views

app_name = 'what_to_do_app'

urlpatterns = [
    # Main site
    path('', views.index, name='index'),
    # Delete task site
    path('task/<int:pk>/delete', views.task_delete, name='task-delete'),
    # Update task site
    path('task/<int:entry_id>/task_update.html', views.task_update, name='task-update')
]