# Generated by Django 2.2 on 2021-04-29 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0004_auto_20210429_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='payment_due',
        ),
    ]
