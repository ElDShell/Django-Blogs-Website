# Generated by Django 5.1.2 on 2024-10-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_rename_creation_date_blog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='media/blog-img/'),
        ),
    ]
