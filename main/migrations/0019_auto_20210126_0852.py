# Generated by Django 3.1.3 on 2021-01-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210126_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default.png', upload_to='blog', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='logo',
            field=models.ImageField(upload_to='partners', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='portfolio', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='services',
            name='img',
            field=models.ImageField(upload_to='services', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='siteconfig',
            name='phone2',
            field=models.BigIntegerField(default='Company phone2', max_length=20),
        ),
        migrations.AlterField(
            model_name='siteconfig',
            name='site_logo',
            field=models.ImageField(upload_to='site_conf', verbose_name='Site Logo'),
        ),
    ]
