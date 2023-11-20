from django.contrib import admin
from registration.models import regi

class regiadmin(admin.ModelAdmin):

    list_display=('name','contact','adhar','address')

admin.site.register(regi,regiadmin)

# Register your models here.
