# Generated by Django 4.0.2 on 2022-02-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0003_salesorder_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='img',
        ),
        migrations.AddField(
            model_name='salesorder',
            name='img_url',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
    ]
