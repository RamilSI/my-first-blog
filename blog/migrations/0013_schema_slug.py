# Generated by Django 4.0.5 on 2022-11-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_schema'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]