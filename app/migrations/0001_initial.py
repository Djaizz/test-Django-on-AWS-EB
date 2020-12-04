from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = ()

    operations = \
        migrations.CreateModel(
            name='M0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f0', models.CharField(max_length=255)),
            ]
        ), \
        migrations.CreateModel(
            name='M1',
            fields=[
                ('m0_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.M0')),
                ('f1', models.CharField(max_length=255)),
            ],
            bases=('app.m0',)
        )
