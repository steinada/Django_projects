from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ("time_of_creation",)


admin.site.register(Todo, TodoAdmin)
