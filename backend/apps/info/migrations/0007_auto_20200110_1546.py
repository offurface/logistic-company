# Generated by Django 2.2.8 on 2020-01-10 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20200103_0400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street',
        ),
        migrations.AddField(
            model_name='address',
            name='label',
            field=models.CharField(default='', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='address',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='address',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='goodscount',
            name='transport_full',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goods_count', to='info.TransportFull', verbose_name='Загруженный транспорт'),
        ),
    ]