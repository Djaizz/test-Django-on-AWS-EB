from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField


class M0(Model):
    f0 = CharField(max_length=255)


class M1(M0):
    f1 = CharField(max_length=255)

    def __str__(self):
        return f'{self.f0} | {self.f1}'


class M(Model):
    fk = ForeignKey(M1, on_delete=CASCADE, related_name='fk')
    m2m = ManyToManyField(M1, related_name='m2m')
    o2o = OneToOneField(M1, on_delete=CASCADE, related_name='o2o')

    def __str__(self):
        return
