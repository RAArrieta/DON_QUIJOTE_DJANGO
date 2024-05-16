from django.contrib.auth.views import LoginView
from django.contrib.auth.views import login_required
from django.shortcuts import render
from .forms import CustomAuthenticationForm

@login_required
def home (request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

