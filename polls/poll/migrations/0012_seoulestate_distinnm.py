# Generated by Django 4.2.2 on 2023-06-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0011_alter_seoulestate_bdcont_alter_seoulestate_bdnm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seoulestate',
            name='distinnm',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
