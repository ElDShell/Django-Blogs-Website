# Generated by Django 5.1.2 on 2024-10-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_fblink_profile_instlink_profile_lilink_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_team_member',
            field=models.BooleanField(default=False),
        ),
    ]
