# Generated by Django 4.1.4 on 2022-12-22 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('summary', models.TextField(default='Thats cool')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address_1', models.CharField(max_length=128, verbose_name=[])),
                ('address_2', models.CharField(blank=True, max_length=128, verbose_name=[])),
                ('city', models.CharField(default='Zanesville', max_length=64, verbose_name=[])),
                ('zip_code', models.CharField(default='43701', max_length=5, verbose_name=[])),
                ('thing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.thing')),
            ],
        ),
    ]
