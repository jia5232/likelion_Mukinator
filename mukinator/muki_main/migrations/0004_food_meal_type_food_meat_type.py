# Generated by Django 4.0.5 on 2022-06-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muki_main', '0003_rename_spicy_food_hot'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='meal_type',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AddField(
            model_name='food',
            name='meat_type',
            field=models.CharField(default='', max_length=2, verbose_name='고기 종류'),
        ),
    ]