# Generated by Django 3.1.3 on 2021-02-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_comments_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('public', 'Published')], max_length=10),
        ),
        migrations.AlterField(
            model_name='comments',
            name='status',
            field=models.CharField(choices=[('public', 'Published')], max_length=10),
        ),
    ]
