from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category__name']
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity']
    list_filter = ['status', ]
    search_fields = ['customer__first_name', 'customer__last_name']


# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
