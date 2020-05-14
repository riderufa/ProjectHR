# Generated by Django 3.0.5 on 2020-05-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(verbose_name='текст ответа')),
                ('valid_answer', models.BooleanField(verbose_name='валидность ответа')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.TextField(verbose_name='текст вопроса')),
                ('type_question', models.IntegerField(choices=[(1, 'Mono'), (2, 'Multi')], verbose_name='тип вопроса')),
                ('image_question', models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение')),
                ('time_limit_question', models.IntegerField(blank=True, null=True, verbose_name='предельное время (сек)')),
                ('answers_question', models.ManyToManyField(related_name='question', to='poll.Answer')),
            ],
        ),
    ]
