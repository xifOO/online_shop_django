# Generated by Django 4.0.2 on 2022-02-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0006_remove_salesorder_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='description',
            field=models.CharField(default='Hello', max_length=255),
        ),
    ]
