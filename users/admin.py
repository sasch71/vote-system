
# Register your models here.

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

def reset_score(modeladmin, request, queryset):
    queryset.update(score=1000)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'score', 'getChoices']
    actions = [reset_score]


admin.site.register(CustomUser, CustomUserAdmin)