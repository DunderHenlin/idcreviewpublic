# Generated by Django 2.2.13 on 2021-03-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
