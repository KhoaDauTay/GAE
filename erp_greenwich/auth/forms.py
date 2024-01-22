from casbin_adapter.models import CasbinRule
from django.forms import ModelForm


class CasbinForm(ModelForm):
    class Meta:
        model = CasbinRule
        fields = ["ptype", "v0", "v1"]
