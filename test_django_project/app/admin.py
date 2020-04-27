from django.contrib.admin import ModelAdmin, register

from .models import M1


@register(M1)
class M1Admin(ModelAdmin):
    pass
