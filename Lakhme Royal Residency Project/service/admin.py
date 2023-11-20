from django.contrib import admin

# Register your models here.

from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('servoce_icon','service_title')

admin.site.register(Service,ServiceAdmin)