# Generated by Django 3.0.5 on 2020-05-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0031_auto_20200509_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='checked_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='valid_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
