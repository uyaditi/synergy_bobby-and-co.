# Generated by Django 3.2.4 on 2022-04-06 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrantinfo',
            name='email_association_href',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registrantinfo',
            name='organization_association_href',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
