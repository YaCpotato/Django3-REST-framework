# Generated by Django 3.0.5 on 2020-04-03 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='注文番号'),
        ),
    ]
