from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Backend running 🚀"})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),
    path('login/', include('Login.urls')),
    path('training/', include('Training.urls')),
    path('certificate/', include('Certificate.urls')),
    path('enrollment/', include('Enrollment.urls')),
]