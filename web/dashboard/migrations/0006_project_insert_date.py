# Generated by Django 3.2.4 on 2023-07-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='insert_date',
            field=models.DateTimeField(default='2023-06-06'),
            preserve_default=False,
        ),
    ]
