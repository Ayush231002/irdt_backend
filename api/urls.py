from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from .views import create_admin

# ✅ Root URL
def home(request):
    return JsonResponse({
        "status": "Backend running",
        "admin": "/admin/"
    })

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    # ✅ your custom route
    path('create-admin/', create_admin),

    # ✅ app routes
    path('api/', include('api.urls')),
    path('login/', include('Login.urls')),
    path('training/', include('Training.urls')),
    path('enrollment/', include('Enrollment.urls')),
    path('certificate/', include('Certificate.urls')),  # (add this if needed)
]