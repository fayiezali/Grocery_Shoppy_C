# Generated by Django 4.2.2 on 2023-07-17 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_rename_pro_user_profile_model_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_model',
            old_name='user',
            new_name='pro_User',
        ),
    ]
