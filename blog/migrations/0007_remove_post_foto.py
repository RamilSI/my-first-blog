# Generated by Django 4.0.5 on 2022-10-19 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_category_alter_post_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='foto',
        ),
    ]
