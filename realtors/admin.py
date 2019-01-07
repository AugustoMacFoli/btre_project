from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    readonly_fields = ('image_tag',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    fields = ('name', 'photo', 'image_tag', 'description', 'phone', 'email', 'is_mvp', 'hire_date')

admin.site.register(Realtor, RealtorAdmin)