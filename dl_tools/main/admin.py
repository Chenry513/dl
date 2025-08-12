from django.contrib import admin
from .models import ModelInfo, UserPreference

@admin.register(ModelInfo)
class ModelInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'use_cases', 'practices', 'colored_severity', 'formatted_concerning_practices_urls')
    search_fields = ('name', 'organization')
    list_filter = ('severity',)  # Optional: This adds a filter for severity in the admin interface

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'model', 'preference')
    search_fields = ('user__username', 'model__name')
    list_filter = ('user', 'model')