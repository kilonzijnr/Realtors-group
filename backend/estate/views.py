from django.shortcuts import render,redirect,get_object_or_404
from .forms import PropertyForm,CommentsForm
from .models import Property,Comments
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

   
    return render(request, 'property/property.html', { "props":props ,"form":form,"comments":comments})
    



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


def add_comment_to_post(request, pk):
    post = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('props', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_comments.html', {'form': form})