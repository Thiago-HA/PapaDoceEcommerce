# Generated by Django 2.2.5 on 2022-12-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20221107_1624'),
        ('produto', '0011_auto_20221108_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='usuarios',
            field=models.ManyToManyField(related_name='produtos', to='usuarios.Usuario'),
        ),
    ]
