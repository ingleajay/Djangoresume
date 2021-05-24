from django.contrib import admin
from .models import ResumeUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(ResumeUser, UserAdmin)
UserAdmin.fieldsets += (
    "Custom Detail:", {'fields': (
        'city', 'country', 'gender', 'profile_image',), }
),
