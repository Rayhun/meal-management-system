from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View #add this


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
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, "Unsuccessful login. Invalid information.")
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)
	# if request.method == "POST":
	# 	form = AuthenticationForm(request, data=request.POST)
	# 	if form.is_valid():
	# 		username = form.cleaned_data.get('username')
	# 		password = form.cleaned_data.get('password')
	# 		user = authenticate(username=username, password=password)
	# 		if user is not None:
	# 			login(request, user)
	# 			messages.info(request, f"You are now logged in as {username}.")
	# 			return redirect("main:homepage")
	# 		else:
	# 			messages.error(request,"Invalid username or password.")
	# 	else:
	# 		messages.error(request,"Invalid username or password.")
	# form = AuthenticationForm()
	# return render(request=request, template_name="main/login.html", context={"login_form":form})