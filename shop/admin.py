from django.contrib import admin
from shop.models import *

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('address',)

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_supply', 'manufacturer_name')
    list_display_links = ('id', 'date_supply')
    list_filter = ('manufacturer__name',)
    ordering = ('-date_supply',)

    @admin.display(description='manufacturer_name')
    def manufacturer_name(self, obj):
        return obj.manufacturer.name


@admin.register(Pos_supply)
class PosSupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'supply', 'quantity')
    list_display_links = ('id',)
    search_fields = ('product__name', 'supply__manufacturer__name')
    list_editable = ('quantity',)
    list_filter = ('supply__manufacturer__name',)
    ordering = ('-supply__id',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_surname', 'customer_name', 'customer_patronymic', 'creation_date', 'delivery_date')
    list_display_links = ('customer_surname', 'customer_name', 'customer_patronymic')
    search_fields = ('customer_surname', 'customer_name', 'delivery_address')
    list_editable = ('delivery_date',)
    list_filter = ('delivery_type',)
    ordering = ('-creation_date',)


@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'discount')
    list_display_links = None
    search_fields = ('product__name', 'order__id')
    list_editable = ('product', 'quantity', 'discount')
    ordering = ('-order__id',)

@admin.register(Parameter)
class ParametersAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Pos_parameter)
class Pos_parameterAdmin(admin.ModelAdmin):
    list_display = ('product', 'parameter', 'value')
    search_fields = ('product__name', 'parameter__name')
    list_editable = ('value',)
    ordering = ('-product__name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available_to_purchase', 'category')
    search_fields = ('name', )
    list_editable = ('price', 'available_to_purchase')
    list_filter = ('available_to_purchase', 'category')
    ordering = ('-created_at',)
