# Generated by Django 3.2.7 on 2021-09-14 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegrambot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountstable',
            options={'managed': False, 'verbose_name': 'Счета', 'verbose_name_plural': 'Счета'},
        ),
        migrations.AlterModelOptions(
            name='childcategorytable',
            options={'managed': False, 'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='itemtable',
            options={'managed': False, 'verbose_name': 'Ключевые слова', 'verbose_name_plural': 'Ключевые слова'},
        ),
    ]