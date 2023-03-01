from django.urls import path,include
from . views import todo,update_task,delete_task,complete_task

urlpatterns = [
    
    path('todo/',todo,name="todo"),
    path('todo/<int:pk>/update_task/',update_task,name="update_task"),
    path('todo/<int:pk>/delete_task/',delete_task,name="delete_task"),
    path('complete_task/<int:task_id>/', complete_task, name='complete_task'),
]
