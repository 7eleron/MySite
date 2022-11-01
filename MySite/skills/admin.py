from django.contrib import admin
from .models import Skills


# Register your models here.
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level',)
    list_display_links = ('skill',)
    fields = ('skill', 'level',)


admin.site.register(Skills, SkillsAdmin)
