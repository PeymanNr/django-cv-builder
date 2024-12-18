# Generated by Django 5.1.3 on 2024-12-01 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='certificates',
            field=models.TextField(blank=True, verbose_name='Certificates'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.TextField(blank=True, verbose_name='Education'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job_experience',
            field=models.TextField(blank=True, default=datetime.datetime(2024, 12, 1, 13, 58, 39, 538092, tzinfo=datetime.timezone.utc), verbose_name='Job Experience'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, related_name='profiles', to='profile.skill'),
        ),
    ]
