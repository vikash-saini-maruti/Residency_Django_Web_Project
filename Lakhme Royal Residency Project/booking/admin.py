from django.contrib import admin


from booking.models import Booking


class bookingadmin(admin.ModelAdmin):
    list_display = ('name','email','check_in','room_type')
    
admin.site.register(Booking,bookingadmin)

#
# 
# 
# # Register your models here.





