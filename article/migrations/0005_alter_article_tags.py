# Generated by Django 4.2.16 on 2024-10-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_articlelike_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Course'), (2, 'Tools'), (3, 'Project'), (4, 'Wood'), (5, 'How-to'), (6, 'Book')], default=0),
        ),
    ]
