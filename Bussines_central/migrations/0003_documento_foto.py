# Generated by Django 5.1.1 on 2024-11-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bussines_central', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
    ]