# Generated by Django 5.1.3 on 2024-12-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_alter_profile_bio_alter_profile_certificates_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='profile.skill'),
        ),
    ]
