# Generated by Django 3.2.12 on 2022-02-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Номер телефона'),
        ),
    ]