# Generated by Django 5.0.6 on 2024-08-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_client_faxclient_alter_client_numcleint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='NumCleint',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
