from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .forms import NewsUserForm, PasswordChangeingForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.admin.forms import PasswordChangeForm


class PasswordChangeView(PasswordChangeView):
	form_class = PasswordChangeingForm
	# form_class = PasswordChangeForm
	success_url = reverse_lazy('password-success')
	# success_url = reverse_lazy('home')


def password_success(request):
	return render(request, 'main/password_success.html', {})


def register_request(request):
	if request.method == "POST":
		form = NewsUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewsUserForm()
	return render(request=request, template_name="main/register.html", context={"form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})


class NewsView(TemplateView):
	template_name = 'news.html'


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("/")