# Generated by Django 3.2.7 on 2021-11-30 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstablecimientoEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=50, verbose_name='Nombre corto')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Rol del establecimiento',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('years', models.CharField(max_length=10, verbose_name='Edad')),
                ('job', models.CharField(choices=[('1', 'No docente'), ('0', 'Docente')], max_length=50, verbose_name='Cargo')),
                ('EstablecimientoEducativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.establecimientoeducativo')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personales',
            },
        ),
    ]
