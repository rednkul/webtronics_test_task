from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser




@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'username', 'is_staff', 'is_confirmed',)
    list_filter = ('email', 'is_staff', 'is_confirmed', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Разрешения', {'fields': ('is_staff', 'is_confirmed',)}, ),
        ('Группы', {'fields': ('groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)



