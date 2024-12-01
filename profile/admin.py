from django.contrib import admin
from django.contrib.admin import register
from profile.models import Profile, Skill


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'job_experience')


@register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
