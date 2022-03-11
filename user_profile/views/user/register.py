from django.views.generic import View
from django.shortcuts import render, redirect
from user_profile.forms.user import NewUserForm
from django.contrib import messages


class RegisterView(View):
    """" User Registration """
    template_name = 'user/register.html'

    def get(self, request):
        form = NewUserForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(
                request, '''
                    Your account has been created! You are now able to log in
                    '''
            )
            return redirect('dashboard')
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information."
            )
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)
