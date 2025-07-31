
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_primer_app.urls')),
        # Include the app's URLs
]
