# Generated by Django 4.0.5 on 2022-11-21 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_report_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_schema', models.CharField(max_length=200)),
                ('category_shcem', models.CharField(max_length=200)),
                ('first_layer', models.CharField(max_length=200)),
                ('dry_residue_first_layer', models.PositiveSmallIntegerField()),
                ('second_layer', models.CharField(max_length=200)),
                ('thikness_first_layer', models.PositiveSmallIntegerField()),
                ('dry_residue_second_layer', models.PositiveSmallIntegerField()),
                ('thikness_second_layer', models.PositiveSmallIntegerField()),
                ('all_thikness', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.ManyToManyField(to='blog.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
