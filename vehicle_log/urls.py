"""vehicle_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView
from vehicle import urls as vehicle_urls
from staff import urls as staff_urls
from vehicle_api import urls as veh_api
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('welcome/', TemplateView.as_view(template_name='users/apps.html'), name='welcome-screen'),
    path('vehicle/', include(vehicle_urls, namespace='vehicle')),
    path('staff/', include(staff_urls, namespace='staff')),
    # path('', include(router.urls)),
    path('api/', include(veh_api, namespace='veh-api')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
