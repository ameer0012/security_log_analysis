from django.contrib import admin
from .models import LogEvent, LogParsingRule

# Register your models here.
admin.site.register(LogEvent)


@admin.register(LogParsingRule)
class LogParsingRuleAdmin(admin.ModelAdmin):
    list_display = ('log_source_type',)


