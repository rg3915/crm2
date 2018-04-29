from django.contrib import admin
from .managers import PersonManager, CustomerManager
from .models import Person, Phone, Customer


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhoneInline]
    objects = PersonManager()
    list_display = ('__str__', 'active')
    search_fields = ('first_name', 'last_name',)
    # form = PersonForm
    actions = None

    # def photo_img(self, obj):
    #     return '<img width="32px" src="{}" />'.format(obj.photo)
    # photo_img.allow_tags = True
    # photo_img.short_description = 'foto'

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Customer)
class CustomerAdmin(PersonAdmin):
    objects = CustomerManager()
    # list_display = ('__str__', 'photo_img', 'email', 'customer_type', 'active')
    list_display = ('__str__', 'active')
    # form = CustomerForm
    actions = None

    # def save_model(self, request, obj, form, change):
    #     obj.person_type = 'c'
    #     super(CustomerAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
