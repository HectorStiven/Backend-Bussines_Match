# Generated by Django 5.1.1 on 2024-10-02 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bussines_central', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
