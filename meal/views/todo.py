from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
)
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from meal.models.market import ToDo, NeedItem
from meal.forms import ToDoForm, NeedItemFormSet


class TodoListView(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, ListView
):
    """ View for the todo list """
    model = ToDo
    template_name = 'meal/todo/list.html'
    context_object_name = 'todos'
    permission_required = 'meal.view_todo'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)


class TodoCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin,
    CreateView
):
    """ View for creating a new todo """
    model = ToDo
    template_name = 'meal/todo/create.html'
    permission_required = 'meal.add_todo'
    form_class = ToDoForm
    success_url = reverse_lazy('meal:dashboard')

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)

    def get_context_data(self, **kwargs):
        """ Add the formset to the context """
        context = super().get_context_data(**kwargs)
        context['formset'] = NeedItemFormSet(
            queryset=NeedItem.objects.none(), prefix='need_item'
        )
        return context

    def post(self, request, *args, **kwargs):
        """ Handle the post request """
        form = self.get_form()
        formset = NeedItemFormSet(
            self.request.POST, queryset=NeedItem.objects.none(),
            prefix='need_item'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.created_user = self.request.user
            form.save()
            need_item = formset.save(commit=False)
            # Delete Object
            for obj in formset.deleted_objects:
                obj.delete()
            # Need Item Create
            for item in need_item:
                item.todo = form
                item.created_user = self.request.user
                item.save()
            return redirect(self.success_url)
        else:
            context = {
                'form': form,
                'formset': formset,
            }
            return render(request, self.template_name, context)


class TodoUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin,
    UpdateView
):
    """ View for updating a todo """
    model = ToDo
    template_name = 'meal/todo/create.html'
    permission_required = 'meal.change_todo'
    form_class = ToDoForm
    success_url = reverse_lazy('meal:dashboard')

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)

    def get_context_data(self, **kwargs):
        """ Add the formset to the context """
        context = super().get_context_data(**kwargs)
        context['formset'] = NeedItemFormSet(
            queryset=NeedItem.objects.filter(todo=self.object),
            prefix='need_item'
        )
        return context

    def post(self, request, *args, **kwargs):
        """ Handle the post request """
        self.object = self.get_object()
        form = self.get_form()
        formset = NeedItemFormSet(
            self.request.POST, queryset=NeedItem.objects.filter(
                todo=self.object
            ), prefix='need_item'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.updated_user = self.request.user
            form.save()
            need_item = formset.save(commit=False)
            # Delete Object
            for obj in formset.deleted_objects:
                obj.delete()
            # Need Item Create
            for item in need_item:
                item.todo = form
                item.updated_user = self.request.user
                item.save()
            return redirect(self.success_url)
        else:
            context = {
                'form': form,
                'formset': formset,
            }
            return render(request, self.template_name, context)

    def form_valid(self, form):
        """ Set the user to the current user """
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class TodoDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin,
    DetailView
):
    """ View for the todo detail """
    model = ToDo
    template_name = 'meal/todo/detail.html'
    permission_required = 'meal.view_todo'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)
