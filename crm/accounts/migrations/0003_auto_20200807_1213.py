# Generated by Django 3.1 on 2020-08-07 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_ordeer_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ordeer',
            new_name='Order',
        ),
    ]
