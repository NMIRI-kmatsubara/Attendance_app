from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from .models import Practice, Place, User

# Register your models here.

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
        (_('Personal info'),{'fields':('first_name', 'last_name')}),
        (_('Permissions'),{'fields':('is_active', 'is_staff', 'is_superuser',
                                 'groups', 'user_permissions')}),  
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
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)




admin.site.register(Practice, PracticeAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(User, MyUserAdmin)