"""User admin classes."""

# Django
from django.contrib import admin

# Import_export
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Models
from letras.models import (
    Profile,
    Suscriptor,
    User,
    Section,
    Notice,
    Picture,
    Images,
    Podcast,
    Columns,
)

# Forms
from django import forms
from django.forms.models import BaseInlineFormSet

class PicturesFormSet(BaseInlineFormSet):
    """Form set to ensure principal picture."""

    def clean(self):
        """Validate duplicate content in module."""
        super().clean()
        data = self.cleaned_data
        if len(data[0]):
            # Ensure principal image for notice
            had_principal = False
            for image in data:
                if image.get('is_principal', False):
                    had_principal = True
            if not had_principal:
                raise forms.ValidationError(
                    'Favor seleccione cuál imagen es la principal.')
        else:
            raise forms.ValidationError(
                'No se puede publicar noticia sin imagenes')

class PhotoResource(resources.ModelResource):
    class Meta:
        model=Picture

@admin.register(Picture)
class PhotoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PhotoResource

class PhotosAdminInline(admin.StackedInline):
    model = Picture
    extra = 1
    formset = PicturesFormSet


class NoticeResource(resources.ModelResource):
    class Meta:
        model = Notice

@admin.register(Notice)
class NoticeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class= NoticeResource
    inlines = [PhotosAdminInline]
    list_display = ('title', 'section', 'priority')
    list_filter = ['section__name', 'priority']
    search_fields = ('title', 'section__name', 'text', 'lead')

@admin.register(Columns)
class ColumnsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    """Url generator for single image admin."""

    list_display = ('title', 'url',)
    list_display_links = ('title',)

    search_fields = ('route', 'title')

    def url(self, obj):
        return obj

    url.short_description = "url"


admin.site.register(Podcast)
admin.site.register(Section)
admin.site.register(Suscriptor)
admin.site.register(Profile)
