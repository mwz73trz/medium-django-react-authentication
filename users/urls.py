from django.urls import include, path
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
]