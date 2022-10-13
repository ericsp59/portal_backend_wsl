from django.contrib import admin
from .models import PortalFrontSettings, Note, PortalGlpiSettings, PortalSemaphoreSettings

# Register your models here.
admin.site.register(PortalFrontSettings)
admin.site.register(PortalGlpiSettings)
admin.site.register(PortalSemaphoreSettings)
admin.site.register(Note)
