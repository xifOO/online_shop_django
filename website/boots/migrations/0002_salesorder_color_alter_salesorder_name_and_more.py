# Generated by Django 4.0.2 on 2022-02-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='color',
            field=models.CharField(default='color', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='price',
            field=models.IntegerField(),
        ),
    ]
