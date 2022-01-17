from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm ,PropertyForm,CommentsForm,RegisterForm
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect,get_object_or_404
from .models import Property,Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user doesnt exist')

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')

    context = {
        'page':page
    }
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    page = 'register'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    context = {
        'form':form,
        'page':page
    }

    return render(request, 'accounts/register.html', context)

@login_required(login_url='login')
def profile(request):
    """User Profile functionality"""
    context = {

    }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile_update.html', context)

@login_required(login_url='login')
def home(request):
    """
    function to render homepage
    """
    props = Property.objects.all()
    return render(request, "client.html", {"props": props})

def adminp(request):
    """
    function to render homepage
    """
    props = Property.objects.all()
    return render(request, "seller.html", {"props": props})



@login_required(login_url='login')
def add_roperty(request):
    """[property functiom]
    Args:
        request ([function]): [function to create new property]
    """
    if request.method == "POST":
        form = PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            new_prop = form.save(commit=False)
            new_prop.save()
        return redirect("adminp")
    else:
        form = PropertyForm()
    return render(request, "new_property.html", {"form": form})

@login_required(login_url='login')
def props(request,id):
    props=Property.objects.get(id=id)
    
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            
            props=Property.objects.all()
            comment=form.save(commit=False)
            
            
            comment.save()
            return redirect('props',id)
    else:
        form=CommentsForm()

    comments= Comments.objects.all()

   
    return render(request, 'property.html', { "props":props ,"form":form,"comments":comments})

@login_required(login_url='login')
def add_comment_to_post(request, pk):
    post = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('props', pk=post.pk)
    else:
        form = CommentsForm()
    return render(request, 'blog/blog_comments.html', {'form': form})