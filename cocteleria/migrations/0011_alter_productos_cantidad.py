# Generated by Django 4.2.1 on 2023-06-24 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocteleria', '0010_alter_productos_cantidad_alter_productos_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]