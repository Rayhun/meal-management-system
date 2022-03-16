from django.contrib import admin
from user_profile.models.profile.profile import Profile
from user_profile.models.profile.education import Education, Skill, University


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'dob', 'mobile', 'address', 'profile_pic']
    search_fields = ['user', 'dob', 'mobile', 'address']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['result']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']
