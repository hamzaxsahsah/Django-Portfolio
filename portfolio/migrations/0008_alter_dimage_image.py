# Generated by Django 4.2.18 on 2025-01-29 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_dimage_project_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
