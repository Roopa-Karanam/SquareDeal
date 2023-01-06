from django.contrib import admin

# Register your models here.

from.models import Thing, Client
admin.site.register(Client)
admin.site.register(Thing)

