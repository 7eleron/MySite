from django.contrib import admin
from .models import PersonalInformation


# Register your models here.
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('info', 'data',)
    list_display_links = ('info',)
    fields = ('info', 'data',)


admin.site.register(PersonalInformation, PersonalInformationAdmin)
