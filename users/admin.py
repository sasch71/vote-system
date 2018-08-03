
# Register your models here.
from django import forms
from .models import CustomUser
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#def reset_score(modeladmin, request, queryset):
#    queryset.update(score=1000)
#
#
#



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password',  'email', 'isPartner', 'isPartner2','isSeniorDirector','isManager','isAdmin','isStaff','score','scoreBus','scoreStrat','scoreOp','scoreManag','scoreTech','scoreDev',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username','email', 'score','scoreBus','scoreStrat','scoreOp','scoreManag','scoreTech','scoreDev',)
    list_filter = ('isPartner', 'isPartner2','isSeniorDirector','isManager','isAdmin','isStaff',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Scores', {'fields': ('score','scoreBus','scoreStrat','scoreOp','scoreManag','scoreTech','scoreDev',)}),
        ('Permissions', {'fields': ('isPartner', 'isPartner2','isSeniorDirector','isManager','isAdmin','isStaff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)

admin.site.unregister(Group)