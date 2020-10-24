from django.contrib import admin
from . models import *

# Register your models here.
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    list_filter = ('user', 'avatar')
    search_fields = ('user', 'avatar')

admin.site.register(Profil, ProfilAdmin)