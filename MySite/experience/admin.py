from django.contrib import admin
from .models import Experience


# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('date_start', 'date_end', 'position', 'responsibilities', 'company', )
    list_display_links = ('company', )
    list_editable = ('position', 'responsibilities', )
    fields = ('company', 'date_start', 'date_end', 'position', 'responsibilities', )


admin.site.register(Experience, ExperienceAdmin)
