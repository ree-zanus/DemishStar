# Generated by Django 4.2.6 on 2023-11-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.TextField(default='', verbose_name='Полное описание'),
            preserve_default=False,
        ),
    ]