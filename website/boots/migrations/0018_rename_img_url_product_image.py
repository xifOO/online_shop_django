# Generated by Django 4.0.2 on 2022-02-16 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0017_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img_url',
            new_name='image',
        ),
    ]