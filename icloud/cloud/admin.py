from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from cloud.forms import ArchiveForm
from cloud.models import Image, Archive


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    fields = ['name', 'description', 'image', 'date']
    list_display = ['name', 'description', 'image', 'date']
    readonly_fields = ['date',]

@admin.register(Archive)
class AdminArchive(admin.ModelAdmin):
    form = ArchiveForm
    list_display = ['title', 'icon']
    filter_horizontal = ['images',]