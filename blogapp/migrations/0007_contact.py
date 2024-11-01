# Generated by Django 5.1.2 on 2024-10-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_alter_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('fblink', models.URLField()),
                ('twlink', models.URLField()),
                ('ytlink', models.URLField()),
                ('instlink', models.URLField()),
            ],
        ),
    ]
