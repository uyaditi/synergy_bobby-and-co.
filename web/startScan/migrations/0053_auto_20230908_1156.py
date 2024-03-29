# Generated by Django 3.2.4 on 2023-09-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0052_s3bucket_perm_all_users_write_acl'),
    ]

    operations = [
        migrations.AddField(
            model_name='s3bucket',
            name='num_objects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='s3bucket',
            name='owner_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='s3bucket',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
