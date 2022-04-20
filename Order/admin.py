from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart',)
    search_fields = ('title',)


admin.site.register(Order, OrderAdmin)
