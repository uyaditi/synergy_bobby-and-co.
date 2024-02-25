# Generated by Django 3.2.4 on 2022-04-20 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0001_initial'),
        ('startScan', '0021_scanhistory_error_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscan',
            name='engine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scanEngine.enginetype'),
        ),
    ]
