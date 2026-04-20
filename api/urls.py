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

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    # ✅ Only include if exists
    path('api/', include('api.urls')),  
    path('login/', include('Login.urls')),
    path('training/', include('Training.urls')),
    path('enrollment/', include('Enrollment.urls')),
]
