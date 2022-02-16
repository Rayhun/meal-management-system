from django.shortcuts import  render, redirect
from meal.forms.user import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("dashboard")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="user/register.html", context={"register_form":form})
