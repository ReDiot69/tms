# Generated by Django 4.0.4 on 2022-07-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='measurement',
            name='category',
            field=models.ManyToManyField(to='customer.category'),
        ),
    ]