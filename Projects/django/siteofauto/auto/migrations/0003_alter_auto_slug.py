# Generated by Django 4.2.1 on 2024-11-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0002_alter_auto_options_auto_slug_alter_auto_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]