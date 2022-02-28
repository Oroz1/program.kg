# Generated by Django 3.2.12 on 2022-02-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_ratetypes_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersstatus',
            name='slug',
            field=models.SlugField(default=None, verbose_name='Slug название'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Вычисление с учетом налога'),
        ),
    ]
