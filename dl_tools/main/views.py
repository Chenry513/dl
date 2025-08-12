import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import ModelInfo


def index(request):
    """Render the single page app entry point."""
    return render(request, 'index.html')


@ensure_csrf_cookie
def set_csrf_token(request):
    """
    Sets the CSRF token cookie.
    """
    return JsonResponse({'detail': 'CSRF cookie set'})


@login_required
def auth_check(request):
    """
    Checks if the user is authenticated.
    """
    return JsonResponse({'authenticated': True})


@csrf_exempt
def register_view(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        form = UserCreationForm({
            'username': data.get('username'),
            'password1': data.get('password'),
            'password2': data.get('password'),
            'email': data.get('email')
        })
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(data.get('password'))
            user.save()
            login(request, user)
            return JsonResponse({'message': 'User registered and logged in successfully'}, status=200)
        return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def login_view(request):
    """
    Handles user login.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully'})
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def logout_view(request):
    """
    Handles user logout.
    """
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})