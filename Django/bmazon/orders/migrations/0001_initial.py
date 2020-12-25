# Generated by Django 3.1.1 on 2020-12-07 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_auto_20201021_0005'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyConversion',
            fields=[
                ('conversion_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_curr', models.CharField(max_length=45)),
                ('to_curr', models.CharField(max_length=45)),
                ('rate', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('estimated_delivery', models.DateTimeField(blank=True, null=True)),
                ('received_date', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cust', to='accounts.account')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_prod', to='products.product')),
            ],
        ),
    ]
