from umb.admin.models import Weight
from django.contrib import admin

# Register your models here.

class WeightAdmin(admin.ModelAdmin):
    actions = (
        'duplicate',
    )

    def duplicate(modeladmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    duplicate.short_description = "Duplicate selected record"
admin.site.register(Weight, WeightAdmin)