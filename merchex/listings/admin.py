from django.contrib import admin

from listings.models import Band
from listings.models import Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'type', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingsAdmin)
