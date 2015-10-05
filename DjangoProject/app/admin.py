from django.contrib.admin import ModelAdmin, site
from models import Dummie


class DummyModelAdmin(ModelAdmin):
    fieldsets = ('Dummy Fields', dict(fields=('dummy_field',))),
    list_display = 'dummy_field',
    search_fields = 'dummy_field',

site.register(Dummie, DummyModelAdmin)
