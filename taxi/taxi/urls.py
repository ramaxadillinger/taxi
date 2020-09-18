from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('adminka/', admin.site.urls),
    path('', include('main.urls')),
]
