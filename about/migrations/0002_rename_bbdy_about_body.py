# Generated by Django 4.2.16 on 2024-10-12 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='bbdy',
            new_name='body',
        ),
    ]
