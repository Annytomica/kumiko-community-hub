# Generated by Django 4.2.16 on 2024-10-12 16:29

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('contact_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]