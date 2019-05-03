from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date')
    list_display_links = ('id','name','email')
    search_fields = ('name','email','contact_date')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)