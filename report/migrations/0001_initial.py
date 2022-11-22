# Generated by Django 4.0.5 on 2022-11-21 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0009_schema_delete_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brend', models.CharField(max_length=255)),
                ('name_item', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
                ('defect_name', models.CharField(max_length=255)),
                ('defect_text', models.TextField()),
                ('remarks', models.TextField()),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('image_tsp', models.ImageField(upload_to='photos-tsp/%Y/%m/%d/')),
                ('spec_dok', models.TextField()),
                ('inference', models.TextField()),
                ('inspector', models.CharField(max_length=255)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.client')),
            ],
        ),
    ]
