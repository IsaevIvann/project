from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from src.users.models import User, Team
from django.contrib.auth.models import Group


@admin.register(User)
class AdminUserAdmin(UserAdmin):
    list_display = (
        "first_name",
        "last_name",
        "username",
        "email",
        "get_status",
        "get_verified",
        "date_joined",
    )
    list_display_links = ("first_name", "last_name", "username")
    list_filter = ("status", "verified_user", "date_joined")
    ordering = ("-date_joined",)
    search_fields = ("username", "email", "vuz_name", "first_name", "last_name")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Дата создания", {"fields": ("date_joined",)}),
        ("Личная информация", {"fields": ("first_name", "last_name", "email", "phone_number", "vuz_name", "organization_link")}),
        ("Статус", {"fields": ("status", "verified_user")}),
        ("Права доступа", {"fields": ("is_staff", "groups", "user_permissions")}),
    )

    readonly_fields = ("date_joined",)

    actions = ["toggle_status", "toggle_verification"]

    @admin.display(boolean=True, description="Верифицирован")
    def get_verified(self, obj):
        return obj.verified_user

    @admin.display(description="Статус")
    def get_status(self, obj):
        return "Активный" if obj.status == "active" else "Неактивный"

    def toggle_status(self, request, queryset):
        for user in queryset:
            user.status = "inactive" if user.status == "active" else "active"
            user.save()
        self.message_user(request, "Статус пользователей успешно изменён.")
    toggle_status.short_description = "Изменить статус пользователей"

    def toggle_verification(self, request, queryset):
        for user in queryset:
            user.verified_user = not user.verified_user
            user.save()
        self.message_user(request, "Верификация пользователей успешно изменена.")
    toggle_verification.short_description = "Верифицировать пользователя"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "is_verified", "rating", "status")
    list_filter = ("is_verified", "status")
    search_fields = ("name", "organization")
    ordering = ("-rating",)

    actions = ["toggle_verification", "toggle_status"]

    def toggle_verification(self, request, queryset):
        for team in queryset:
            team.is_verified = not team.is_verified
            team.save()
        self.message_user(request, "Верификация команды успешно изменена.")
    toggle_verification.short_description = "Верифицировать команду"

    def toggle_status(self, request, queryset):
        for team in queryset:
            team.status = "inactive" if team.status == "active" else "active"
            team.save()
        self.message_user(request, "Статус команды успешно изменён.")
    toggle_status.short_description = "Изменить статус команды"


admin.site.unregister(Group)


admin.site.site_header = "Панель администратора"
admin.site.site_title = "Управление Moot Court"
admin.site.index_title = "Добро пожаловать в панель администратора"
