from django.contrib import admin

from .models import Aniversario

class AniversarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')

admin.site.register(Aniversario, AniversarioAdmin)