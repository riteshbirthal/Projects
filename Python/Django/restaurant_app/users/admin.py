from django.contrib import admin
from .models import Profile, UserCart, UserOrder

# Register your models here.


admin.site.register((Profile, UserCart))
@admin.register(UserOrder)
class UserCartAdmin(admin.ModelAdmin):
    readonly_fields = ["user", "items", "ordered_on", "total"]
