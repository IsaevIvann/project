from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team

admin.site.register(User,UserAdmin)



class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ("name", "organization", "is_verified", "rating", "status", "owner")
    filter_horizontal = ("members",)


admin.site.register(Team,TeamAdmin)