from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Save data to the database
        user = User(username=username, email=email, password=password)
        user.save()

        return redirect(reverse('exchange_app:exchange'))
    else:
        return render(request, 'main/registration.html')

# @login_required
# def mainn(request):
#     if request.user.is_authenticated:
#         # Render the main page if user is authenticated
#         return redirect(reverse('exchange_app:exchange'))
#     else:
#         # Redirect to login page if user is not authenticated
#         return redirect('main/registration.html')

# def logout_view(request):
#     logout(request)
#     return redirect('main:register')