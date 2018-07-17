# Generated by Django 2.0.7 on 2018-07-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20180716_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='isAdmin',
        ),
        migrations.RemoveField(
            model_name='question',
            name='isManagers',
        ),
        migrations.RemoveField(
            model_name='question',
            name='isPartener2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='isPartner',
        ),
        migrations.RemoveField(
            model_name='question',
            name='isSeniorDirector',
        ),
        migrations.RemoveField(
            model_name='question',
            name='isStaff',
        ),
        migrations.AddField(
            model_name='question',
            name='isadmin',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ismanagers',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ispartener2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ispartner',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='isseniordirector',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='isstaff',
            field=models.BooleanField(default=True),
        ),
    ]