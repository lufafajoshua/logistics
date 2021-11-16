from django.contrib import admin

from .models import Account, Location, Contact, Services

admin.site.register(Account)
admin.site.register(Location)
admin.site.register(Contact)
admin.site.register(Services)
