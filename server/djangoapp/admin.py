from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarMake


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields=['model', 'dealer_id', 'name', 'model_type', 'year']
    # inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']


# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)