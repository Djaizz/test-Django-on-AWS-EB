from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import \
    ForeignKey, ManyToManyField, OneToOneField

from model_utils.models import TimeStampedModel
from polymorphic.models import PolymorphicModel


class M0(PolymorphicModel, TimeStampedModel):
    f0 = CharField(
            verbose_name='Field 0',
            help_text='Field 0',
            max_length=255,
            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta:
        verbose_name = 'M0'
        verbose_name_plural = 'M0s'

        db_table = 'M0'

        default_related_name = 'm0s'

        ordering = 'f0',

    def __str__(self):
        return f'{type(self).__name__} #{self.id} | F0: {self.f0}'


class M1(M0):
    f1 = CharField(
            verbose_name='Field 1',
            help_text='Field 1',
            max_length=255,
            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta:
        verbose_name = 'M1'
        verbose_name_plural = 'M1s'

        db_table = 'M1'

        default_related_name = 'm1s'

        ordering = 'f1',

    def __str__(self):
        return f'{type(self).__name__} #{self.id} | ' \
               f'F0: {self.f0} | F1: {self.f1}'


class M1A(M0):
    m1a_m0_ptr = OneToOneField(
            # verbose_name=...,
            # help_text=...,

            to=M0,
            on_delete=CASCADE,
            limit_choices_to={},
            related_name='m1a',
            related_query_name='m1a',
            # to_field=...,
            db_constraint=True,
            swappable=True,
            parent_link=True,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=False,
            # error_messages=None,
            primary_key=True,
            unique=True,   # implied
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    f1a = CharField(
            verbose_name='Field 1a',
            help_text='Field 1a',
            max_length=255,
            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta:
        verbose_name = 'M1A'
        verbose_name_plural = 'M1As'

        db_table = 'M1A'

        default_related_name = 'm1as'

        ordering = 'f1a',

    def __str__(self):
        return f'{type(self).__name__} #{self.id} | ' \
               f'F0: {self.f0} | F1A: {self.f1a}'


class M2(M1):
    f2 = CharField(
            verbose_name='Field 2',
            help_text='Field 2',
            max_length=255,
            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta:
        verbose_name = 'M2'
        verbose_name_plural = 'M2s'

        db_table = 'M2'

        default_related_name = 'm2s'

        ordering = 'f2',

    def __str__(self):
        return f'{type(self).__name__} #{self.id} | ' \
               f'F0: {self.f0} | F1: {self.f1} | F2: {self.f2}'


class M2A(M1A):
    f2a = CharField(
            verbose_name='Field 2a',
            help_text='Field 2a',
            max_length=255,
            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta:
        verbose_name = 'M2A'
        verbose_name_plural = 'M2As'

        db_table = 'M2A'

        default_related_name = 'm2as'

        ordering = 'f2a',

    def __str__(self):
        return f'{type(self).__name__} #{self.id} | ' \
               f'F0: {self.f0} | F1A: {self.f1a} | F2A: {self.f2a}'


class M2B(M1, M1A):
    f2b = CharField(
            verbose_name='Field 2b',
            help_text='Field 2b',
            max_length=255,
            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta:
        verbose_name = 'M2B'
        verbose_name_plural = 'M2Bs'

        db_table = 'M2B'

        default_related_name = 'm2bs'

        ordering = 'f2b',

    def __str__(self):
        return f'{type(self).__name__} #{self.id} | F0: {self.f0} | ' \
               f'F1: {self.f1} | F1A: {self.f1a} | F2B: {self.f2b}'


class M(TimeStampedModel):
    RELATED_NAME = 'ms'
    RELATED_QUERY_NAME = 'm'

    fk = ForeignKey(
            verbose_name='Foreign Key',
            help_text='Foreign Key',

            to=M0,
            on_delete=CASCADE,
            limit_choices_to={},
            related_name=f'fk_{RELATED_NAME}',
            related_query_name=f'fk_{RELATED_QUERY_NAME}',
            # to_field=...,
            db_constraint=True,
            swappable=True,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    o2o = OneToOneField(
            verbose_name='One-to-One',
            help_text='One-to-One',

            to=M0,
            on_delete=CASCADE,
            limit_choices_to={},
            related_name=f'o2o_{RELATED_QUERY_NAME}',
            related_query_name=f'o2o_{RELATED_QUERY_NAME}',
            # to_field=...,
            db_constraint=True,
            swappable=True,
            parent_link=False,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=True,   # implied
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    self_fk = ForeignKey(
            verbose_name='Self Foreign Key',
            help_text='Self Foreign Key',

            to='self',
            on_delete=CASCADE,
            limit_choices_to={},
            related_name=f'fk_{RELATED_NAME}',
            related_query_name=f'fk_{RELATED_QUERY_NAME}',
            # to_field=...,
            db_constraint=True,
            swappable=True,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    self_o2o = OneToOneField(
            verbose_name='Self One-to-One',
            help_text='Self One-to-One',

            to='self',
            on_delete=CASCADE,
            limit_choices_to={},
            related_name=f'o2o_{RELATED_QUERY_NAME}',
            related_query_name=f'o2o_{RELATED_QUERY_NAME}',
            # to_field=...,
            db_constraint=True,
            swappable=True,
            parent_link=False,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=True,   # implied
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    m2m = ManyToManyField(
            verbose_name='Many-to-Many',
            help_text='Many-to-Many',

            to=M0,
            related_name=f'm2m_{RELATED_NAME}',
            related_query_name=f'm2m_{RELATED_QUERY_NAME}',
            limit_choices_to={},
            symmetrical=False,
            # through=...,
            # through_fields=...,
            # db_table=...
            db_constraint=True,
            swappable=True,

            # null=True,   # no effect
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None   # not supported
        )

    asym_self_m2m = ManyToManyField(
            verbose_name='Asymmetrical Self Many-to-Many',
            help_text='Asymmetrical Self Many-to-Many',

            to='self',
            related_name='asym_self_m2ms',
            related_query_name='reverse_asym_self_m2m',
            limit_choices_to={},
            symmetrical=False,
            # through=...,
            # through_fields=...,
            # db_table=...
            db_constraint=True,
            swappable=True,

            # null=True,   # no effect
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None   # not supported
        )

    sym_self_m2m = ManyToManyField(
            verbose_name='Symmetrical Self Many-to-Many',
            help_text='Symmetrical Self Many-to-Many',

            to='self',
            related_name='sym_self_m2ms',
            related_query_name='+',
            limit_choices_to={},
            symmetrical=True,
            # through=...,
            # through_fields=...,
            # db_table=...
            db_constraint=True,
            swappable=True,

            # null=True,   # no effect
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None   # not supported
        )

    class Meta:
        verbose_name = 'M'
        verbose_name_plural = 'Ms'

        db_table = 'M'

        default_related_name = 'ms'

    def __str__(self):
        return f'{type(self).__name__} #{self.id}'
