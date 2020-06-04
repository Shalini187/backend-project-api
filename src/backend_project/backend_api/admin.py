from django.contrib import admin
from . import models

# Register your models here.
class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'request_method', 'request_url',
                    'response_code', 'datetime', 'ip_address')
    date_hierarchy = 'datetime'
    list_filter = ('request_method', 'response_code')
    search_fields = ('user', 'request_url')


admin.site.register(models.ActivityLog, LogAdmin)
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
