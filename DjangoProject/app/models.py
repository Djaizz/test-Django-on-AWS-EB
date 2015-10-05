from django.db.models import Model, CharField


class Dummie(Model):
    dummy_field = CharField(max_length=100)
