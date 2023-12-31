# Generated by Django 4.2.6 on 2023-11-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_clients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AddField(
            model_name='clients',
            name='Comment',
            field=models.TextField(default='', verbose_name='Комментарий'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clients',
            name='Number',
            field=models.CharField(max_length=10, verbose_name='Номер'),
        ),
    ]
