# Generated by Django 2.0.7 on 2018-07-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='score',
            field=models.FloatField(default=1000),
        ),
    ]