# Generated by Django 5.0.4 on 2024-05-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_intro_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='img1',
            field=models.ImageField(upload_to='picture', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='img2',
            field=models.ImageField(upload_to='picture', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='img3',
            field=models.ImageField(upload_to='picture', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='img4',
            field=models.ImageField(upload_to='picture', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='img5',
            field=models.ImageField(upload_to='picture', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='img6',
            field=models.ImageField(upload_to='picture', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='img7',
            field=models.ImageField(upload_to='picture', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='img8',
            field=models.ImageField(upload_to='picture', verbose_name='Image'),
        ),
    ]
