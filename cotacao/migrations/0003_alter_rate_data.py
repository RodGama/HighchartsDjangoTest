# Generated by Django 3.2.8 on 2021-10-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0002_alter_rate_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='data',
            field=models.DateField(),
        ),
    ]
