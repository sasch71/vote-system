# Generated by Django 2.0.7 on 2018-07-17 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180717_0738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='isManagers',
            new_name='isManager',
        ),
    ]
