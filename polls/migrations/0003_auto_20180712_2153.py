# Generated by Django 2.0.7 on 2018-07-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_voters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='voters',
            field=models.CharField(default='', max_length=4000),
        ),
    ]
