from django.urls import path
from .views import *

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