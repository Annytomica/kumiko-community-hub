# Generated by Django 4.2.16 on 2024-10-08 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_articlelike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlelike',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_liker', to=settings.AUTH_USER_MODEL),
        ),
    ]
