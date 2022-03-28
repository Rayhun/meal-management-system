from django.shortcuts import redirect, render
from django.views.generic import CreateView
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

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)

    def post(self, request):
        form = DeposetForm(request.POST)
        self.object = self.get_object()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.is_approved = False
            obj.save()
            return redirect("meal:deposet_list")
        else:
            context = {
                'form': form,
                'object': self.object
            }
            return render(request, self.template_name, context)
