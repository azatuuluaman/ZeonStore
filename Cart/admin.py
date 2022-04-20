from django.contrib import admin
from .models import CartItem, Cart
from Order.models import Order


class OrderItemInLine(admin.TabularInline):
    model = Order


class CartItemInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline, OrderItemInLine]
    list_display = ('user',)


admin.site.register(Cart, CartAdmin)
