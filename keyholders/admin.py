from django.contrib import admin
from .models import State, County, City, Address


# Addresses Inline
# class InlineBusiness(admin.StackedInline):
#     model = Business
#     extra = 1
#     list_display = ( 'city', 'area', 'number', 'directional', 
#         'street_name', 'street_type', 'suffix', 'zipcode',)
#     ordering = ('address',)
#     search_fields = ( 'city', 'area', 'number', 'directional', 
#         'street_name', 'street_type', 'suffix', 'zipcode',)

class AddressAdmin(admin.ModelAdmin):
    # inlines = [InlineBusiness]
    list_editable = ('city', 'area', 'number', 'directional',
        'street_name', 'street_type', 'suffix', 'zipcode',)
    list_display = ('city', 'area', 'number', 'directional', 
        'street_name', 'street_type', 'suffix', 'zipcode',)
    ordering = ('city', 'area', 'number', 'directional', 
        'street_name', 'street_type', 'suffix', 'zipcode',)
    search_fields = ['city__name', 'area', 'number', 'directional', 
        'street_name', 'street_type', 'suffix', 'zipcode',]


# Cities Inline
class InlineAddress(admin.StackedInline):
    model = Address
    extra = 1
    list_display = ('county','name',)
    search_fields = ('name', 'county',)

class CityAdmin(admin.ModelAdmin):
    inlines = [InlineAddress]
    list_display = ('county','name',)
    ordering = ('county', 'name',)
    search_fields = ['county__name', 'name',]


# Counties Inline
class InlineCity(admin.StackedInline):
    model = City
    extra = 1
    list_display = ('state', 'name',)
    ordering = ('name',)

class CountyAdmin(admin.ModelAdmin):
    inlines = [InlineCity]
    list_display = ('state', 'name',)
    ordering = ('state', 'name',)
    search_fields = ['state__name','name',]


# States Inline
class InlineCounty(admin.StackedInline):
    model = County
    extra = 1
    list_display = ('name', 'abbreviation',)
    ordering = ('name',)

class StateAdmin(admin.ModelAdmin):
    inlines = [InlineCounty]
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ['name', 'abbreviation',]


admin.site.register(State, StateAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)

admin.site.site_header = "KeysDu Admin"
admin.site.site_title = "KeysDu Admin Portal"
admin.site.index_title = "Welcome to KeysDu Admin Portal"
