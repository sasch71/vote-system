# Generated by Django 2.0.7 on 2018-07-13 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180713_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choicesrelated', to='polls.Question'),
        ),
    ]
