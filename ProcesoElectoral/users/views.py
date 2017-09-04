from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login

# Create your views here.

class login_user(FormView):
    model = User
    form_class = AuthenticationForm
    template_name = 'login_user.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.get_success_url())