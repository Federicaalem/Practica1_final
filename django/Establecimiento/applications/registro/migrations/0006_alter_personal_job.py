# Generated by Django 3.2.7 on 2021-11-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20211130_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='job',
            field=models.CharField(choices=[('1', 'No Docente'), ('0', 'Docente')], max_length=50, verbose_name='Cargo'),
        ),
    ]
