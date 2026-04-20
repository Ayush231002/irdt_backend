from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# ✅ Root API check
def home(request):
    return JsonResponse({"message": "Backend is running 🚀"})

urlpatterns = [
    path('', home),  # root

    path('admin/', admin.site.urls),

    # App routes
    path('api/', include('api.urls')),
    path('login/', include('Login.urls')),
    path('training/', include('Training.urls')),
    path('certificate/', include('Certificate.urls')),
    path('enrollment/', include('Enrollment.urls')),
]