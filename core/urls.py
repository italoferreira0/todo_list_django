from django.contrib import admin
from django.urls import path

from todos.views import home,TodoListView,TodoCreateView,TodoUpdateView,TodoDeleteView,TodoCompleteView

urlpatterns = [
    path('admin/', admin.site.urls ,name="home"),
    path('', home),
    path('todo_list/',TodoListView.as_view(), name="todo_list"),
    path('create/', TodoCreateView.as_view(), name="todo_create"),
    path('update/<int:pk>', TodoUpdateView.as_view(), name="todo_update"),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name="todo_delete"),
    path('complete/<int:pk>', TodoCompleteView.as_view(), name="todo_complete")

]
