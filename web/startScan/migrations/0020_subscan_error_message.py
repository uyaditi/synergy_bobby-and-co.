# Generated by Django 3.2.4 on 2022-04-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0019_scanactivity_error_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscan',
            name='error_message',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
