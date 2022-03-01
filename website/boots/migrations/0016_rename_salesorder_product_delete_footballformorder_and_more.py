# Generated by Django 4.0.2 on 2022-02-15 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0015_goalkeeperform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SalesOrder',
            new_name='Product',
        ),
        migrations.DeleteModel(
            name='FootballFormOrder',
        ),
        migrations.DeleteModel(
            name='GoalKeeperForm',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Товары'},
        ),
    ]