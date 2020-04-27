from django.db.models import Model
from django.db.models.fields import CharField


class M0(Model):
    f0 = CharField(max_length=255)


class M1(M0):
    f1 = CharField(max_length=255)

    def __str__(self):
        return f'{self.f0} | {self.f1}'
