# Generated by Django 2.0.7 on 2018-07-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='voters',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]