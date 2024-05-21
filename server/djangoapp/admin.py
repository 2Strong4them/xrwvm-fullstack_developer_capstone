# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from django.contrib import admin
from .models import CarMake, CarModel

# Inline class for CarModel
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra forms to display in the inline form

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Columns to display in the list view
    inlines = [CarModelInline]  # Include CarModel inline

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')  # Columns to display in the list view
    list_filter = ('car_make', 'type', 'year')  # Filters to display in the sidebar
    search_fields = ('name', 'car_make__name')  # Fields to search

# Register models with the admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
