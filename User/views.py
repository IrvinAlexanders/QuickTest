from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from rest_framework import permissions
from User.serializers import UserSerializer



class LoginView(auth_views.LoginView):

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    form_class = LoginForm
    template_name = 'user/login.html'


class RegisterView(generic.CreateView):
    
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')
    
def FormValidation(request):
	data = {
		'form': RegisterForm()
	}

	if request.method == 'POST':
		formulario = RegisterForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			username = formulario.cleaned_data['username']
			password = formulario.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect(to='/')
	return render(request,'user/register.html',data)