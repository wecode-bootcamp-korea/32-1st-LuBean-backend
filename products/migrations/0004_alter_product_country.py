# Generated by Django 4.0.4 on 2022-05-03 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.country'),
        ),
    ]
