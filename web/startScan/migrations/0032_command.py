# Generated by Django 3.2.4 on 2023-01-04 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0031_auto_20220910_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('command', models.TextField(blank=True, null=True)),
                ('return_code', models.IntegerField(blank=True, null=True)),
                ('output', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField()),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startScan.scanactivity')),
                ('scan_history', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startScan.scanhistory'))
            ],
        ),
    ]
