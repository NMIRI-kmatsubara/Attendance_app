from django.contrib import admin
from .models import Practice, Place
# Register your models here.

class PracticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    list_display_links = ('id', 'date')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'pl')
    list_display_links = ('id', 'pl')

admin.site.register(Practice, PracticeAdmin)
admin.site.register(Place, PlaceAdmin)
