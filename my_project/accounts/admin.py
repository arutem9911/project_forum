from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['birth_date', 'avatar']


class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.register(User, UserProfileAdmin)
