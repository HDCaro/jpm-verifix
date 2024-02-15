from django.contrib import admin
from .models import Parameter

# Register your models here.


class ParametersAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


admin.site.register(Parameter, ParametersAdmin)