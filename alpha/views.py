from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.utils import timezone

class RegisterFormAuto(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

def home(request):
    context = {}
    return render(request, "home.html",context)

def product(request):
    context = {}
    return render(request, "product.html",context)

def document(request):
    context = {}
    return render(request, "document.html",context)

def about(request):
    context = {}
    return render(request, "about.html",context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 自动登录新注册用户
            return redirect('alpha:home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('alpha:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {'user': user})

def user_logout(request):
    logout(request)
    return redirect('alpha:home')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('alpha:home')
    return render(request, 'delete_account.html')