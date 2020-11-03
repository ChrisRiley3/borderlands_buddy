from django.contrib import admin
from .models import Weapon, Category, Review


class weaponAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'manufacture',
        'price',
        'category',
        'image',
    )


class categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Weapon, weaponAdmin)
admin.site.register(Category, categoryAdmin)
admin.site.register(Review)
