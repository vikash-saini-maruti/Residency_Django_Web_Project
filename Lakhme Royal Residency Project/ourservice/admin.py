from django.contrib import admin


from ourservice.models import Ourservice

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_des')
    

admin.site.register(Ourservice,ServiceAdmin)


# Register your models here.
