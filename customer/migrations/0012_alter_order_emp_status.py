# Generated by Django 4.0.4 on 2022-08-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_order_emp_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='emp_status',
            field=models.CharField(choices=[('NA', 'NA'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED')], default='NA', max_length=25),
        ),
    ]
