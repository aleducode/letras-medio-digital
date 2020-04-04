"""User admin classes."""

# Django
from django.contrib import admin

# Models
from letras.models import (
    Profile,
    Suscriptor,
    User,
    Section,
    Notice,
    Picture
)

# Forms
from django import forms
from django.forms.models import BaseInlineFormSet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'role', 'position', 'picture')
    list_display_links = ('user', 'position')

    search_fields = (
        'user__email',
        'user__first_name'
    )
    list_filter = (
        'created',
        'modified',
        'user__is_active',
    )
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            )
        }),
        ('Extra Info', {
            'fields': (
                ('position', 'role'),
                ('biography'),
            )
        }),
        ('Social Network', {
            'fields': (
                ('facebook'),
                ('instagram'),
                ('twitter'),
                ('linkedin'),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),

            )
        }),
    )
    readonly_fields = ('created', 'modified')


class ProfileInLine(admin.StackedInline):
    """Profile inline admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInLine,)
    model = User
    list_display = ('username', 'email', 'profile', 'is_superuser')


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


class PhotosAdminInline(admin.TabularInline):
    model = Picture
    extra = 1
    formset = PicturesFormSet

    list_filter = ['section__name', 'priority']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Section)

admin.site.register(Suscriptor)
