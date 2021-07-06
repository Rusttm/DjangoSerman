from django.contrib import admin
from .models import *

# Register your models here.
class topMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)

admin.site.register(topMenu)
admin.site.register(topSubMenu)
