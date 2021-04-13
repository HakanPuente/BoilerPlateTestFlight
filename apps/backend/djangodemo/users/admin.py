from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserChangeForm, MyUserCreationForm


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['email', 'username', 'fav_color']

admin.site.register(MyUser, MyUserAdmin)
