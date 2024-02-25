# Generated by Django 3.2.4 on 2022-01-06 04:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VulnerabilityReference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='VulnerabilityTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='vulnerability',
            name='matcher_name',
        ),
        migrations.RemoveField(
            model_name='vulnerability',
            name='reference',
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='cve_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='cvss_metrics',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='cvss_score',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='cwe_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='references',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='template_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='extracted_results',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='http_url',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
    ]
