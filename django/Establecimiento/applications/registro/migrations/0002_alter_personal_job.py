# Generated by Django 3.2.7 on 2021-11-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='job',
            field=models.CharField(choices=[('0', 'Docente'), ('1', 'No docente')], max_length=50, verbose_name='Cargo'),
        ),
    ]
