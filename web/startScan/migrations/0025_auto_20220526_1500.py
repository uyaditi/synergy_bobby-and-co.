# Generated by Django 3.2.4 on 2022-05-26 15:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0024_auto_20220526_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directoryscan',
            name='command_line',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='extracted_results',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5000), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='http_url',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
