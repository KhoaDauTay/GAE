# Register your models here.
from casbin_adapter.models import CasbinRule
from django.contrib import admin

from erp_greenwich.auth.forms import CasbinForm


@admin.register(CasbinRule)
class CasbinAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        return CasbinForm
