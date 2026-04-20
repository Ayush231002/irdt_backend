from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# ✅ Root URL (no 404)
def home(request):
    return JsonResponse({
        "status": "IRDT Backend Running",
        "admin_url": "/admin/"
    })

urlpatterns = [
    path('', home),  # ✅ root fix
    path('admin/', admin.site.urls),

    # ✅ App routes
    path('api/', include('api.urls')),
    path('login/', include('Login.urls')),
    path('training/', include('Training.urls')),
    path('certificate/', include('Certificate.urls')),
    path('enrollment/', include('Enrollment.urls')),
]
