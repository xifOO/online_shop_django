# Generated by Django 4.0.2 on 2022-02-19 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0026_remove_product_img_url_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='img_url',
        ),
    ]
