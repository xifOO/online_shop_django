# Generated by Django 4.0.2 on 2022-02-10 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0005_alter_salesorder_img_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='color',
        ),
    ]