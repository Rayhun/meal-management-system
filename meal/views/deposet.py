from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# local import
from meal.models import Deposet
from meal.forms import DeposetForm


class DeposetCerateView(
    LoginRequiredMixin, UserPassesTestMixin, CreateView
):
    """ Creat6e Deposet """
    model = Deposet
    template_name = "deposet/create.html"
    form_class = DeposetForm
    permission_required = 'meal.add_deposet'
    success_url = reverse_lazy("meal:deposet_list")

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)

    def post(self, request):
        form = DeposetForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.is_approved = False
            obj.save()
            return redirect(self.success_url)
        else:
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)


class DeposetUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    """ Creat6e Deposet """
    model = Deposet
    template_name = "deposet/create.html"
    form_class = DeposetForm
    permission_required = 'meal.add_deposet'
    success_url = reverse_lazy("meal:deposet_list")

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)


class DeposetListView(
    LoginRequiredMixin, UserPassesTestMixin, ListView
):
    """ Deposet List """
    model = Deposet
    template_name = "deposet/list.html"
    permission_required = 'meal.list_deposet'

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)
