# Generated by Django 3.0.5 on 2020-06-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0007_auto_20200605_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='null', upload_to='articulos'),
        ),
    ]
