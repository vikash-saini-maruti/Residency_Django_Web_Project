from django.contrib import admin


from Product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name','Disc','Price','Quantity')
    

admin.site.register(Product,ProductAdmin)


# Register your models here.
