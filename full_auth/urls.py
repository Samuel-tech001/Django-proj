
from django.contrib import admin
from django.urls import path, include
from .views import send_test_email, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    path('', home, name='home'),
    path('send-email/', send_test_email, name='send_test_email'),
]
