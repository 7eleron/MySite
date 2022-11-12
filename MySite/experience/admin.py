from django.contrib import admin
from .models import Experience


# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'date_start', 'date_end', 'position', 'stack', 'responsibilities', )
    list_display_links = ('company', )
    list_editable = ('position', 'responsibilities', 'stack', )
    fields = ('date_start', 'date_end', 'position', 'responsibilities', 'stack', 'company', )


admin.site.register(Experience, ExperienceAdmin)
