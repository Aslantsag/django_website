# Generated by Django 3.1.3 on 2021-01-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default.png', upload_to='', verbose_name='image'),
        ),
    ]
