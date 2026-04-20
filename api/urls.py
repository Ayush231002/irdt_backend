from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from django.urls import path
from .views import create_admin

urlpatterns = [
    path('create-admin/', create_admin),
]

# ✅ Root URL
def home(request):
    return JsonResponse({
        "status": "Backend running",
        "admin": "/admin/"
    })

