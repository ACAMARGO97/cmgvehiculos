# Generated by Django 4.0.4 on 2022-05-18 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.BigIntegerField()),
                ('vehiculos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculos')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('valorTotal', models.BigIntegerField()),
                ('tipoPago', models.CharField(max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehiculos', models.ManyToManyField(through='ventas.VehiculoVenta', to='vehiculos.vehiculos')),
            ],
        ),
        migrations.AddField(
            model_name='vehiculoventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta'),
        ),
    ]
