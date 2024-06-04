# Generated by Django 5.0.4 on 2024-05-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footwearapp', '0013_viewallproduct_delete_category_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='products/')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
