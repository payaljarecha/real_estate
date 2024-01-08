from django.urls import path
from .views import property_listing, tenant_management

urlpatterns = [
    path('', property_listing, name='property_listing'),  # Set default view for root URL
    path('property_listing/', property_listing, name='property_listing'),
    path('tenant_management/', tenant_management, name='tenant_management'),
    # Add other URLs as needed
]