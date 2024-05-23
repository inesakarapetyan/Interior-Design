# Generated by Django 5.0.4 on 2024-05-07 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_project_delete_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Picture')),
                ('img', models.ImageField(blank=True, upload_to='picture', verbose_name='Image')),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='proj', to='main.project')),
            ],
        ),
    ]