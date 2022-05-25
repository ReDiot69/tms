# Generated by Django 4.0.3 on 2022-05-18 10:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=25)),
                ('number', models.IntegerField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoulder', models.FloatField()),
                ('full_length', models.FloatField()),
                ('chest', models.FloatField()),
                ('hip', models.FloatField()),
                ('sl', models.FloatField()),
                ('m', models.FloatField()),
                ('ah', models.FloatField()),
                ('open', models.FloatField()),
                ('thigh', models.FloatField()),
                ('knee', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdate', models.DateField(default=datetime.date.today)),
                ('deadline', models.DateField()),
                ('customer_measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.measurement')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
