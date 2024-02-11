"""
URL configuration for BankApplication project.
"""
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from app.views import ContractView

urlpatterns = [
    path('api/contracts/', ContractView.as_view({'post': 'create'})),
    path('api/contracts/<int:pk>/mabufactures/', ContractView.as_view({'get': 'retrieve'})),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]