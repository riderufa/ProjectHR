# Generated by Django 3.0.5 on 2020-05-07 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0023_checkedanswer_valid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkedanswer',
            old_name='valid',
            new_name='checked',
        ),
    ]
