from django.contrib import admin
from meal.models.profile.profile import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'dob', 'mobile', 'address', 'profile_pic']
    search_fields = ['user', 'dob', 'mobile', 'address', 'profile_pic']
