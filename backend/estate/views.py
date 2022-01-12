from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from backend.estate.models import Location 
# Create your views here.
@login_required(login_url='login')
def search_location(request):
    if 'search_location' in request.GET and request.GET['search_location']:
        name = request.GET.get("search_user")
        results = Location.search_location(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'location.html', params)
    else:
        message = "Location not found"
    return render(request, 'location.html', {'message': message})
