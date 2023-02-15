from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/', include('carts.urls')),
    path('api/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/v1/', include('home.routes')),
    path('api/accounts/', include('accounts.urls')),
]
