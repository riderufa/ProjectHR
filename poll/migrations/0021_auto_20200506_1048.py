# Generated by Django 3.0.5 on 2020-05-06 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0020_auto_20200505_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkedanswer',
            name='checked',
            field=models.BooleanField(blank=True, null=True, verbose_name='валидность ответа'),
        ),
        migrations.AlterField(
            model_name='checkedanswer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='poll.CheckedQuestion'),
        ),
        migrations.AlterField(
            model_name='checkedanswer',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='текст ответа'),
        ),
    ]
