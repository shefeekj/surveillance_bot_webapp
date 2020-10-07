from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.
# This function will return and render the home page when url is http://localhost:8000/to_do/.

@login_required(login_url='/login')
def index_page(request):
    # Get the index template file absolute path.
    # index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    print("Reached here")
    return render(request, 'home.html')
