# Generated by Django 4.0.2 on 2022-02-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0023_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]