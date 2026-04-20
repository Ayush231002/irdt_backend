from django.shortcuts import render

from django.http import JsonResponse
from Login.models import User

def create_admin(request):
    if not User.objects.filter(ehrms_code="admin123").exists():
        User.objects.create_superuser(
            ehrms_code="admin123",
            password="admin123"
        )
        return JsonResponse({"status": "admin created"})
    return JsonResponse({"status": "already exists"})

# Create your views here.
