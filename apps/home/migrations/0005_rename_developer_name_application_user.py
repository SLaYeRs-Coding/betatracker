# Generated by Django 3.2.6 on 2022-05-21 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_developer_name_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='developer_name',
            new_name='user',
        ),
    ]
