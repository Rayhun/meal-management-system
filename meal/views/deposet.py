from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from meal import models

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

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)

