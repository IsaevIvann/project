from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from src.users.models import User, Team
from django.contrib.auth.models import Group


# --- Подраздел "Администраторы" и "ВУЗ/организации" в одном классе ---
@admin.register(User)
class AdminUserAdmin(UserAdmin):
    list_display = (
        "first_name",
        "last_name",
        "date_joined",
        "username",
        "status",
        "email",

    )
    list_filter = (
        "status",
        "date_joined",

    )
    ordering = ("-date_joined",)
    search_fields = ("username", "email", "organization_name", "first_name")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Дата создания", {"fields": ("date_joined",)}),
        ("Личная информация", {"fields": ("first_name", "last_name", "email", "phone_number", "organization_name")}),
        ("Статус", {"fields": ("status", "is_verified")}),
        ("Права доступа", {"fields": ("is_staff", "groups", "user_permissions")}),
    )

    actions = ["toggle_status", "toggle_verification"]

    # Действие для изменения статуса пользователя (активный/неактивный)
    def toggle_status(self, request, queryset):
        for user in queryset:
            user.status = "inactive" if user.status == "active" else "active"
            user.save()
        self.message_user(request, "Статус пользователей успешно изменен.")
    toggle_status.short_description = "Изменить статус пользователей"

    # Действие для изменения статуса верификации пользователя
    def toggle_verification(self, request, queryset):
        for user in queryset:
            user.is_verified = not user.is_verified
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

    # Действие для изменения статуса верификации команды
    def toggle_verification(self, request, queryset):
        for team in queryset:
            team.is_verified = not team.is_verified
            team.save()
        self.message_user(request, "Верификация команды успешно изменена.")
    toggle_verification.short_description = "Верифицировать команду"

    # Действие для изменения статуса команды
    def toggle_status(self, request, queryset):
        for team in queryset:
            team.status = "inactive" if team.status == "active" else "active"
            team.save()
        self.message_user(request, "Статус команды успешно изменен.")
    toggle_status.short_description = "Изменить статус команды"


# --- Удаление стандартной группы Group ---
admin.site.unregister(Group)


# --- Кастомизация заголовков админки ---
admin.site.site_header = "Панель администратора"
admin.site.site_title = "Управление Moot Court"
admin.site.index_title = "Добро пожаловать в панель администратора"
