from django.contrib import admin
from .models import Assortment, Division

class AssortmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measure_unit')

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Assortment, AssortmentAdmin)
admin.site.register(Division, DivisionAdmin)
