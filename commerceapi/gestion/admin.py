from django.contrib import admin
from .models import ProfileOrderproduct, ProfileAddress, ProfileOrder, ProfileCustomer, ShopProduct, ShopSubcategory
from .models import ContactContact

# Register your models here.
admin.site.register(ProfileOrderproduct)
admin.site.register(ProfileAddress)
admin.site.register(ProfileOrder)
admin.site.register(ProfileCustomer)
admin.site.register(ShopProduct)
admin.site.register(ShopSubcategory)
admin.site.register(ContactContact)
