from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import Group

# Create your views here.
def register(request):
    """User Registration Functionality"""
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def profile(request):
    """User Profile functionality"""
    context = {

    }
    return render(request, 'profile.html', context)