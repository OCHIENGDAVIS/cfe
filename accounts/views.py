from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.core.exceptions import  ValidationError
from .models import User
from .forms import UserloginForm


class Register(View):
    template_name = 'accounts/register.html'

    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('products:list'))
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username, password, password2)
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise  ValidationError('User with name username already exists')
        if password != password2:
            raise ValidationError('passwords must match')

        user = User(username=username)
        user.set_password(password)
        user.save()
        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            return HttpResponseRedirect(reverse('products:list'))
        return HttpResponseRedirect(reverse('accounts:login'))

class Login(View):
    template_name = 'accounts/login.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('products:list'))
        form = UserloginForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('products:list'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('products:list'))
        raise ValidationError('Invalid credentials try again')

class Logout(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))

    