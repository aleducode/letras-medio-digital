"""User admin classes"""
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#models
from letras.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    #hace ver los campos que yo quiera en el modelo de user
    list_display = ('pk', 'user','role', 'position', 'picture')
    #crea links de acceso en los mismos campos
    list_display_links = ('user', 'position')
    #editable en la tabla

    #busqueda por campos
    search_fields = (
        'user__email',
        'user__first_name'

    )
    #filtros establecidos por campos
    list_filter = (
        'created',
        'modified',
        'user__is_active',
    )
    #editar visualización de detalle 
    #tupla titulo con diccionario de fields que pueden ser
    #tuplas dependiendo de ubicación
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
    #campos que no se pueden modificar
    readonly_fields=('created','modified')
class ProfileInLine(admin.StackedInline):
    """Profile inline admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines=(ProfileInLine,)
    

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Section)
admin.site.register(Notice)
admin.site.register(Picture)
admin.site.register(Suscriptors)
admin.site.register(Metrics)
    
