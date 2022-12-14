# Generated by Django 4.0.6 on 2022-08-17 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_front', '0007_portalglpisettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portalfrontsettings',
            options={'verbose_name': 'Настройка', 'verbose_name_plural': 'Настройки semaphore git'},
        ),
        migrations.AlterModelOptions(
            name='portalglpisettings',
            options={'verbose_name': 'Настройка', 'verbose_name_plural': 'Настройки GLPI API'},
        ),
        migrations.AddField(
            model_name='portalglpisettings',
            name='glpi_srv_name',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя'),
        ),
    ]
