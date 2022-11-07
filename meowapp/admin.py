from django.contrib import admin
from .models import *

# Register your models here.

class BeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'date_added', 'key', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('key', 'price', 'title', 'date_added')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'message', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('beat', 'date')
    list_display_links = ('date', 'beat')
    search_fields = ('beat', 'date')

admin.site.register(Genre)
admin.site.register(Key)
admin.site.register(Beat, BeatAdmin)
admin.site.register(ContactUs, ContactAdmin)
# admin.site.register(Order, OrderAdmin)