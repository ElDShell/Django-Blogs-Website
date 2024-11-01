# Generated by Django 5.1.2 on 2024-10-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fblink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instlink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lilink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twlink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
