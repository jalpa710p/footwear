# Generated by Django 5.0.4 on 2024-07-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footwearapp', '0042_delete_addimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomenImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='womenimage/')),
            ],
        ),
    ]
