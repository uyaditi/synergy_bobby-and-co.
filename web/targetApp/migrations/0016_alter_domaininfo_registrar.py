# Generated by Django 3.2.4 on 2022-06-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0015_auto_20220615_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='registrar',
            field=models.ManyToManyField(blank=True, to='targetApp.DomainRegistrar'),
        ),
    ]
