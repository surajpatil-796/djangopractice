
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            un = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('pwd')
            user = authenticate(username=un, password=pwd)
            if user:
                login(request, user)
                print(user)
                return redirect("/")
            else:
                msg = "Invalid credentials"
                context['msg'] = msg
    return render(request, "accounts/login.html", context)

def logout_page(request):
    logout(request)
    return redirect("/")

# Create your views here.
def register_page(request):
    form = RegisterForm(request.POST or None)
    message=""
    if request.method == 'POST':
        if form.is_valid():
            un = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pwd = form.cleaned_data.get('pwd')
            user = User.objects.create_user(username=un, email=email, password=pwd)
            if user:
                form = RegisterForm()
                message = "User Registered Successfully."
    return render(request, "accounts/register.html", {'form':form, 'msg': message})



