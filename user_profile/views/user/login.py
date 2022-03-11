from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View


class LoginView(View):
    """" User Login """
    template_name = 'user/login.html'

    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('meal:dashboard')
            else:
                messages.error(request, 'Your account is not active.')
                return redirect('user:login')
        else:
            messages.error(request, "Unsuccessful login Invalid information.")
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)
