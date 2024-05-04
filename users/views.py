from django.shortcuts import render,redirect
from .forms import Signup
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import Signup
from django.urls import reverse_lazy
from .models import ProfileData

# Create your views here.
class RegisterClassView(CreateView):
    model = ProfileData
    form_class = Signup
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account successfuly created')
        return response


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profilepage(request):
    return render(request, 'profile.html')
