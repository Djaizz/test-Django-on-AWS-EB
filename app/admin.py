from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from django_model_query_graphs import PK_FIELD_NAME, ModelQueryGraph

from silk.profiling.profiler import silk_profile

from .models import M0, M1, M1A, M2, M2A, M2B, M


@register(M0)
class M0Admin(ModelAdmin):
    list_display = \
        '_str', \
        'modified'

    list_display_links = '_str',

    search_fields = '_str',

    show_full_result_count = False

    def _str(self, obj):
        return str(obj)

    @silk_profile(name=f'{__module__}: {M0._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M0._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M1)
class M1Admin(ModelAdmin):
    list_display = \
        '_str', \
        'modified'

    list_display_links = '_str',

    search_fields = '_str',

    show_full_result_count = False

    def _str(self, obj):
        return str(obj)

    @silk_profile(name=f'{__module__}: {M1._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M1._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M1A)
class M1AAdmin(ModelAdmin):
    list_display = \
        '_str', \
        'modified'

    list_display_links = '_str',

    search_fields = '_str',

    show_full_result_count = False

    def _str(self, obj):
        return str(obj)

    @silk_profile(name=f'{__module__}: {M1A._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M1A._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M2)
class M2Admin(ModelAdmin):
    list_display = \
        '_str', \
        'modified'

    list_display_links = '_str',

    search_fields = '_str',

    show_full_result_count = False

    def _str(self, obj):
        return str(obj)

    @silk_profile(name=f'{__module__}: {M2._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M2._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M2A)
class M2AAdmin(ModelAdmin):
    list_display = \
        '_str', \
        'modified'

    list_display_links = '_str',

    search_fields = '_str',

    show_full_result_count = False

    def _str(self, obj):
        return str(obj)

    @silk_profile(name=f'{__module__}: {M2A._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M2A._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M2B)
class M2BAdmin(ModelAdmin):
    list_display = \
        '_str', \
        'modified'

    list_display_links = '_str',

    search_fields = '_str',

    show_full_result_count = False

    def _str(self, obj):
        return str(obj)

    @silk_profile(name=f'{__module__}: {M2B._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M2B._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M)
class MAdmin(ModelAdmin):
    list_display = \
        '_str', \
        'modified'

    list_display_links = '_str',

    search_fields = '_str',

    show_full_result_count = False

    def _str(self, obj):
        return str(obj)

    @silk_profile(name=f'{__module__}: {M._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)
