from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import TodoForm
from .models import Todos


class UserListView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = User.objects.all()
        q = self.request.GET.get('queryset')
        if q:
            queryset = queryset.filter(Q(username__contains=q))
        return queryset


@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('/')
    else:
        form = TodoForm()
    return render(request, 'todo/todos_new.html', {"form": form})


def todo_list(request):
    # Assuming Todo.objects is a manager
    todos = Todos.objects.all()
    return render(request, 'todo/todo-list.html', {'todos': todos})


# views.py
class TodoListView(ListView):
    template_name = 'todo/this-user.html'
    context_object_name = 'clay'

    def get_queryset(self):
        try:
            pk = self.kwargs['pk']
            queryset = Todos.objects.filter(user=pk)
        except:
            queryset = Todos.objects.all()
        return queryset


class TodoUpdateView(UpdateView):
    model = Todos
    template_name = 'todo/todo_update.html'
    fields = ['title', 'description', 'start_time', 'end_time', 'status']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Todo successfully updated!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('this-user', kwargs={'pk': self.object.pk})


class TodoDeleteView(DeleteView):
    model = Todos
    template_name = 'todo/delete_todo.html'
    success_url = reverse_lazy('home')
