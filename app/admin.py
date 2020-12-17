from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from django_model_query_graphs import PK_FIELD_NAME, ModelQueryGraph

from silk.profiling.profiler import silk_profile

from .models import M0, M1, M1A, M2, M2A, M2B, M


@register(M0)
class M0Admin(ModelAdmin):
    list_display = \
        'f0', #\
        # 'modified'

    # list_display_links = 'f0',

    # search_fields = 'f0',

    show_full_result_count = False

    def get_queryset(self, request):
        query_set = super().get_queryset(request=request)

        return query_set \
            if request.resolver_match.url_name.endswith('_change') \
          else query_set.only(*self.list_display)

    @silk_profile(name=f'{__module__}: {M0._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M0._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M1)
class M1Admin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {M1._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M1._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M1A)
class M1AAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {M1A._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M1A._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M2)
class M2Admin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {M2._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M2._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M2A)
class M2AAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {M2A._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M2A._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M2B)
class M2BAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {M2B._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M2B._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(M)
class MAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {M._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {M._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)
