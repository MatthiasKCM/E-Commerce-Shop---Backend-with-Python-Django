# Generated by Django 4.2.7 on 2023-11-29 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartmanager', '0003_rename_gross_total_cart_cart_gross_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_gross_total',
        ),
    ]
