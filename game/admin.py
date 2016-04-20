from django.contrib import admin
from game.models import Character, Portal, Room
# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    #readonly_fields = ('user',)
    list_display   = ('id', 'user', 'name', 'overview_description', 'room', 'avatar')
    list_filter    = ('id', 'user', 'name', 'description', 'room')
    ordering       = ('id', )
    search_fields  = ('id', 'user', 'name', 'description', 'room')
    list_editable = ('name', )
    list_display_links = ('id', )

    fieldsets = (
    # Fieldset 1 : meta-info
   ('meta-info', {
        'classes': ['collapse',],
        'fields': ('user', ) #id pas modifiable
    }),
    # Fieldset 2 : contenu
    ('info', {
       'description': ' name, description, room and avatar',
        'classes': ['wide', ],
       'fields': ('name', 'description', 'room', 'avatar',)
    }),
    )


    def overview_description(self, character):
        """
        Retourne les 3 premiers caractères de la description d'un charactère. S'il
        y a plus de 3 caractères, il faut ajouter des points de suspension.
        """
        text = character.description[0:3]
        if len(character.description) > 3:
            return '%s…' % text
        else:
            return text

    # En-tête de notre colonne
    overview_description.short_name = 'Description overview'

    def save_model(self, request, obj, form, change):
        super(CharacterAdmin, self).save_model(request, obj, form, change)

class RoomAdmin(admin.ModelAdmin):
    list_display   = ('id', 'name', )
    list_filter    = ('name', )
    ordering       = ('name', )
    search_fields  = ('name', )
    list_editable = ('name', )
    list_display_links = ('id', )

    fieldsets = (
    ('info', {
        'classes': ['wide', ],
       'fields': ('name', )
    }),
    )

    def save_model(self, request, obj, form, change):
        super(RoomAdmin, self).save_model(request, obj, form, change)

class PortalAdmin(admin.ModelAdmin):
    #readonly_fields = ('entry', 'exit')
    list_display   = ('id', 'is_enable', 'direction', 'entry', 'exit')
    list_filter    = ('is_enable', 'direction', 'entry', 'exit')
    ordering       = ('entry', )
    search_fields  = ('is_enable', 'direction', 'entry', 'exit')
    list_editable = ('is_enable', 'direction', 'entry', 'exit')
    list_display_links = ('id', )

    fieldsets = (
    # Fieldset 1 : meta-info
   ('meta-info', {
        'classes': ['collapse',],
        'fields': ('entry', 'exit', ) #id pas modifiable
    }),
    # Fieldset 2 : contenu
    ('info', {
       'description': ' is_enable and direction',
        'classes': ['wide', ],
       'fields': ('is_enable', 'direction', )
    }),
    )

    def save_model(self, request, obj, form, change):
        super(PortalAdmin, self).save_model(request, obj, form, change)

admin.site.register(Character, CharacterAdmin)
admin.site.register(Portal, PortalAdmin)
admin.site.register(Room, RoomAdmin)