# Generated by Django 3.2.6 on 2021-08-05 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210805_1411'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='items',
            unique_together={('productColor', 'size', 'product_name')},
        ),
    ]