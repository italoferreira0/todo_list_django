from datetime import date

from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView, View
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
from .models import Todo


def home(request):
    return render(request,"todos/home.html")

# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request,"todos/todo_list.html",{"todos":todos})

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        # Todo.objects.get(pk=pk)
        todo = get_object_or_404(Todo, pk=pk)
        # todo.finished_at = date.today()
        # todo.save()
        todo.mark_has_complete()
        return redirect("todo_list")

    