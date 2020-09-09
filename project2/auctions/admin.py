from django.contrib import admin
from .models import *


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'starting_bid')


admin.site.register(Category)
admin.site.register(AuctionListening, AuctionAdmin)
