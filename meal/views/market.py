from datetime import date
from django.views.generic import (
    ListView, View, UpdateView, DetailView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
)
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from meal.models.market import Market, Item
from meal.forms import ItemFormSet


class MarketListView(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, ListView
):
    """ View for the market list """
    model = Market
    template_name = 'meal/market/list.html'
    context_object_name = 'markets'
    permission_required = 'meal.view_market'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)


class MarketCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin,
    View
):
    """ View for creating a new market """
    model = Market
    template_name = 'meal/market/create.html'
    permission_required = 'meal.add_market'
    success_url = reverse_lazy('meal:market_list')

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)

    def get(self, request):
        """ Handle the get request """
        formset = ItemFormSet(
            queryset=Item.objects.none(), prefix='formset'
        )
        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        """ Handle the post request """
        formset = ItemFormSet(
            self.request.POST, queryset=Item.objects.none(),
            prefix='formset'
        )
        if formset.is_valid():
            obj = self.model.objects.create(
                user=request.user,
                date=date.today()
            )
            formsets = formset.save(commit=False)
            for obj in formset.deleted_objects:
                obj.delete()
            for form in formsets:
                form.item = obj
                form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'formset': formset})
