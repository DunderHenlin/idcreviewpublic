# Generated by Django 2.2.13 on 2021-03-23 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_profile_dpabout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
