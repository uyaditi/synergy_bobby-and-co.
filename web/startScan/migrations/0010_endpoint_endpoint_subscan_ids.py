# Generated by Django 3.2.4 on 2022-03-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0009_vulnerability_matcher_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='endpoint_subscan_ids',
            field=models.ManyToManyField(related_name='endpoint_subscan_ids', to='startScan.SubScan'),
        ),
    ]
