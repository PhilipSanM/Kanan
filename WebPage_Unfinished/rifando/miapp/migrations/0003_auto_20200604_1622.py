# Generated by Django 3.0.5 on 2020-06-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_auto_20200604_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Email'),
        ),
    ]
