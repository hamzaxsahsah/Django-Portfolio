# Generated by Django 4.2.18 on 2025-01-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_persone_github_persone_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='articale',
            field=models.TextField(blank=True),
        ),
    ]
