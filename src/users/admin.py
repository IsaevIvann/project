
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team
from django.contrib.auth.models import Group

@admin.register(User)
class AdminUserAdmin(UserAdmin):

    list_display = ("first_name", "last_name", "date_joined", "username", "status", "email")
    list_filter = ("status", "date_joined")
    ordering = ("-date_joined",)
    search_fields = ("username", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Дата создания", {"fields": ("date_joined",)}),
        ("Личная информация", {"fields": ("first_name", "last_name", "email")}),
        ("Статус", {"fields": ("status",)}),
        ("Права доступа", {"fields": ("is_staff","groups", "user_permissions")}), #, "groups", "user_permissions"

    )

    actions = ["toggle_status"]

    def toggle_status(self, request, queryset):

        for user in queryset:
            if user.status == "active":
                user.status = "inactive"
            else:
                user.status = "active"
            user.save()
        self.message_user(request, "Статус успешно изменен.")
    toggle_status.short_description = "Изменить статус пользователей"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "organization",)




admin.site.unregister(Group)

class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        "date_joined",
        "organization_name",
        "username",
        "phone_number",
        "email",
        "is_verified",
        "status",
    )
    list_filter = ("is_verified", "status", "date_joined")
    ordering = ("-date_joined",)
    search_fields = ("organization_name", "username", "email")

    actions = ["toggle_verification", "toggle_status"]

    def toggle_verification(self, request, queryset):
        for user in queryset:
            user.is_verified = not user.is_verified
            user.save()
        self.message_user(request, "Верификация пользователей успешно изменена.")
    toggle_verification.short_description = "Верифицировать пользователя"

    # def toggle_status(self, request, queryset):
    #     for user in queryset:
    #         if user.status == "active":
    #             user.status = "inactive"
    #         else:
    #             user.status = "active"
    #         user.save()
    #     self.message_user(request, "Статус пользователей успешно изменен.")
    # toggle_status.short_description = "Изменить статус пользователей"


