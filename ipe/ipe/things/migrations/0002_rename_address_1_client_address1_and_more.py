# Generated by Django 4.1.4 on 2022-12-22 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='address_1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='address_2',
            new_name='address2',
        ),
    ]
