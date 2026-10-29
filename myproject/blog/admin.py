from django.contrib import admin

from accounts.models import UserProfile


# Register your models here.


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'l_name')
    search_fields = ('email', 'name', 'l_name')
