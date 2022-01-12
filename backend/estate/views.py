from django.shortcuts import render,redirect
from .forms import PropertyForm
from .models import Property
from django.contrib.auth.decorators import login_required
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




