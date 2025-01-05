from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MootCourt



class MootcourtAdmin(admin.ModelAdmin):
    model = MootCourt
    list_display = ("name", "organizer", )


admin.site.register(MootCourt,MootcourtAdmin)

