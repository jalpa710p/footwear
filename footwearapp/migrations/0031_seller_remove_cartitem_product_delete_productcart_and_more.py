# Generated by Django 5.0.4 on 2024-06-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footwearapp', '0030_productcart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sellers/')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductCart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]