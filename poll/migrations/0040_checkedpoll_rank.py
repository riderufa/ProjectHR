# Generated by Django 3.0.5 on 2020-05-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0039_checkedquestion_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkedpoll',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
