from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'
    fieldsets = (
        ('', {
            'fields': (
                'active', 'slug',
            )
        }),
        ('Documents', {
            'fields': (
                'cpf',
                'rg',
                'cnpj',
                'ie',
            )
        }),
        ('Details', {
            'fields': (
                'photo',
                'birthday',
                'department',
                'info',
                'occupation',
            )

        }),
        ('Address', {
            'fields': ('address', 'address_number', 'complement', 'district', 'city', 'uf', 'cep')
        }),
    )


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'slug', 'email', 'first_name',
                    'last_name', 'is_staff', 'custom_group', 'active')
    list_select_related = ('person', )
    actions = None

    if not settings.DEBUG:
        def has_delete_permission(self, request, obj=None):
            return False

    def custom_group(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''
    custom_group.short_description = 'Grupo'

    def slug(self, obj):
        if obj.person.slug:
            return obj.person.slug
    slug.admin_order_field = 'slug'
    slug.short_description = 'slug'

    def active(self, obj):
        if obj.person.active:
            return obj.person.active
    active.admin_order_field = 'active'
    active.short_description = 'ativo'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
if not settings.DEBUG:
    admin.site.unregister(Group)
