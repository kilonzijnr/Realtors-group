from django.shortcuts import render,redirect
from .forms import PropertyForm
from .models import Property
from django.contrib.auth.decorators import login_required
from django.views.generic import  DetailView
# Create your views here.
def home(request):
    """
    function to render homepage
    """
    props = Property.objects.all()
    return render(request, "home/index.html", {"props": props})
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
        return redirect("home")
    else:
        form = PropertyForm()
    return render(request, "property/new_property.html", {"form": form})





def props(request,id):
    prop = Property.objects.get(id = id)
    return render(request,'property/property.html',{"prop":prop})
 



def blogs_comments(request, id):
    post = BlogPost.objects.get(id = id)
    return render(request, "blog_comments.html", {'post':post}) 

def blog_comments(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post':post, 'comments':comments}) 
