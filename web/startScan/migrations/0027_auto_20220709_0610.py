# Generated by Django 3.2.4 on 2022-07-09 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0026_auto_20220526_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryISO',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='geo_iso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startScan.countryiso'),
        ),
    ]
