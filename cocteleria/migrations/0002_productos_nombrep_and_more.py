# Generated by Django 4.2.1 on 2023-05-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocteleria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='nombrep',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterOrderWithRespectTo(
            name='productos',
            order_with_respect_to='nombrep',
        ),
    ]
