from django.shortcuts import render
from .models import Property
from django.contrib.auth.decorators import login_required
from .forms import  RateForm


# Create your views here.
@login_required
def rate(request, property_id):
    property = Property.objects.get(id=property_id)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.property = property
            rate.save()
        return render(request, 'property.html', locals())
    else:
        form = RateForm()
    return render(request, 'rate.html', locals())
