# Generated by Django 3.2.4 on 2023-04-12 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0028_auto_20230412_0402'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DNSRecords',
            new_name='DNSRecord',
        ),
        migrations.RenameModel(
            old_name='NameServers',
            new_name='NameServer',
        ),
    ]
