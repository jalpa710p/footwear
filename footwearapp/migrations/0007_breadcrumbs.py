# Generated by Django 5.0.4 on 2024-05-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footwearapp', '0006_bestseller_featuredimage_partner_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breadcrumbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='breadcrumbs/')),
            ],
        ),
    ]
