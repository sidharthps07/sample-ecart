from django.contrib import admin

from .models import Products,Offers


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Register your models here.
admin.site.register(Products, ProductAdmin)
admin.site.register(Offers, OfferAdmin)
