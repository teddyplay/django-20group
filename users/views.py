from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import RegistrationForm
from .models import Profile



class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = "/login/"




def profile(request):
    return render(request, 'profile.html')


