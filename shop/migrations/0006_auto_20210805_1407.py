# Generated by Django 3.2.6 on 2021-08-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_products_productname'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='productColor',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='red', max_length=6),
        ),
        migrations.AlterField(
            model_name='items',
            name='size',
            field=models.CharField(choices=[('Large', 'L'), ('Medium', 'M'), ('Small', 'S')], default='S', max_length=6, unique=True),
        ),
        migrations.DeleteModel(
            name='ProductColor',
        ),
    ]
