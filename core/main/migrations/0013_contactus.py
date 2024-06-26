# Generated by Django 5.0.4 on 2024-05-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Your message')),
            ],
        ),
    ]
