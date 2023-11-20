from django.contrib import admin


from review.models import Review

class Reviewadmin(admin.ModelAdmin):
    list_display=('name','star','review','suggestion')
    
    
admin.site.register(Review,Reviewadmin)
# Register your models here.
