from django.contrib import admin
from . import models

# Register your models here.
class LogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'user_location', 'get_period')

class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time')

admin.site.register(models.ActivityLog, LogAdmin)
admin.site.register(models.ActivityPeriod, ActivityPeriodAdmin)
