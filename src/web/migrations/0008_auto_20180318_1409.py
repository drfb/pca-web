# Generated by Django 2.0 on 2018-03-18 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_databaseconfig_inactive_database'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DatabaseConfig',
        ),
        migrations.RemoveField(
            model_name='pcaprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='wcaprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='PCAProfile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='WCAProfile',
        ),
    ]