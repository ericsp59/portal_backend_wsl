"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from portal_app.views import portal_app

from portal_logs.views import PortalLogsApiView
from portal_front.views import  PortalFrontApiView, PortalGlpiApiView, PortalSemaphoreApiView, PortalGetDevicesFromDbApiView, PortalGetNetDevInfoByIdFromCbApiView, PortalGetPhoneInfoByIdFromDbApiView, PortalGetComputerInfoByIdFromDbApiView, PortalGetDeviceIpByIdFromDbApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portal_app, name='portal_app'),
    path('api/v1/log_list/', PortalLogsApiView.as_view()),
    path('api/v1/add_playbook/', PortalFrontApiView.as_view()),
    path('api/v1/get_glpi_settings/', PortalGlpiApiView.as_view()),
    path('api/v1/get_semaphore_settings/', PortalSemaphoreApiView.as_view()),
    path('api/v1/get_devices/', PortalGetDevicesFromDbApiView.as_view()),
    path('api/v1/get_net_device_info_by_id/', PortalGetNetDevInfoByIdFromCbApiView.as_view()),
    path('api/v1/get_phone_info_by_id/', PortalGetPhoneInfoByIdFromDbApiView.as_view()),
    path('api/v1/get_computer_info_by_id/', PortalGetComputerInfoByIdFromDbApiView.as_view()),
    path('api/v1/get_device_ip_by_id/', PortalGetDeviceIpByIdFromDbApiView.as_view()),
    path('api/v1/', include('portal_front.urls'))

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)