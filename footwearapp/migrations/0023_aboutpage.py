# Generated by Django 5.0.4 on 2024-05-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footwearapp', '0022_womenimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField(verbose_name='Video URL')),
                ('background_image', models.ImageField(upload_to='about/', verbose_name='Background Image')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
    ]
