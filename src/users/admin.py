from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User,UserAdmin)
# admin.site.register(Team,TeamAdmin)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
#
# class UserAdmin(UserAdmin):
#     model = User
#     # fieldsets = UserAdmin.fieldsets + (
#     #     ("Дополнительная информация", {
#     #         "fields": (
#     #             "position", "photo", "description", "organization_name", "organization_link",
#     #             "accepts_invitations", "is_verified", "rating", "phone", "role", "status"
#     #         ),
#     #     }),
#     # )
#     # list_display = ("username", "email", "rating", "verified_user")
#
# # class TeamAdmin(admin.ModelAdmin):
# #     model = Team
# #     list_display = ("name", "organization", "is_verified", "rating", "status", "owner")
# #     filter_horizontal = ("members",)
#
# admin.site.register(User, UserAdmin)
# # admin.site.register(Team, TeamAdmin)
