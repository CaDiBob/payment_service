# Generated by Django 4.1.3 on 2022-11-30 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0002_order_alter_item_currency'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
