# Generated by Django 4.0.2 on 2022-02-26 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0031_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
