# Generated by Django 3.2.8 on 2021-11-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
    ]
