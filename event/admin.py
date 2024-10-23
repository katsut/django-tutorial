from django.contrib import admin

from event.models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    search_fields = ["name"]


admin.site.register(Event, EventAdmin)
