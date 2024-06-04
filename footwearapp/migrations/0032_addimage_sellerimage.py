# Generated by Django 5.0.4 on 2024-06-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footwearapp', '0031_seller_remove_cartitem_product_delete_productcart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='addimage/')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sellerimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sellerimage/')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]