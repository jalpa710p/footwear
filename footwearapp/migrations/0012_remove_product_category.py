# Generated by Django 5.0.4 on 2024-05-29 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footwearapp', '0011_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]