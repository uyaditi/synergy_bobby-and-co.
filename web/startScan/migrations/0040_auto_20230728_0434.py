# Generated by Django 3.2.4 on 2023-07-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0039_auto_20230728_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerability',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='impact',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='remediation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
