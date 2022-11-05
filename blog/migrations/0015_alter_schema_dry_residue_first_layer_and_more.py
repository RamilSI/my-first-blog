# Generated by Django 4.0.5 on 2022-11-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_schema_name_alter_schema_schema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='dry_residue_first_layer',
            field=models.PositiveSmallIntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='schema',
            name='dry_residue_second_layer',
            field=models.PositiveSmallIntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='schema',
            name='thikness_first_layer',
            field=models.PositiveSmallIntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='schema',
            name='thikness_second_layer',
            field=models.PositiveSmallIntegerField(max_length=3),
        ),
    ]
