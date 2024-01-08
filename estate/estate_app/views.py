from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Property, Unit, Tenant

def property_listing(request):
    properties = Property.objects.all()
    return render(request, 'property_listing.html', {'properties': properties})

def tenant_management(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_management.html', {'tenants': tenants})


# Create your views here.
