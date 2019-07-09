from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from .models import Part, Practice, Place, User, Attend, Check_attend

# Register your models here.

class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'part')
    list_display_links = ('id', 'part')

class PracticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    list_display_links = ('id', 'date')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'pl')
    list_display_links = ('id', 'pl')

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        (_('Personal info'),{'fields':('full_name','part')}),
        #(_('Permissions'),{'fields':('is_active', 'is_staff', 'is_superuser',
        #                         'groups', 'user_permissions')}),  
        (_('Important dates'), {'fields':('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'full_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'full_name')
    ordering = ('email',)

class Attemdadmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class Check_attendadmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(Part, PartAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(User, MyUserAdmin)
admin.site.register(Attend, Attemdadmin)
admin.site.register(Check_attend, Check_attendadmin)