# Generated by Django 5.0.7 on 2024-08-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0006_boat_created_at_boat_is_published_owner_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='опубликовано'),
        ),
    ]
