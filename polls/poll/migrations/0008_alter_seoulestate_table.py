# Generated by Django 4.2.2 on 2023-06-26 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0007_rename_seoul_seoulestate_alter_seoulestate_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='seoulestate',
            table='Seoulestate',
        ),
    ]
