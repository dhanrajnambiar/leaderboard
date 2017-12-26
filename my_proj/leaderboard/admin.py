from django.contrib import admin

from .models import participant

class participantAdmin(admin.ModelAdmin):
    list_display = ('full_name','score','time_added')

admin.site.register(participant,participantAdmin)
