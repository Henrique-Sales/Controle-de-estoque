# Generated by Django 5.2 on 2025-05-04 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_pubicada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='pubicada',
            new_name='publicada',
        ),
    ]
