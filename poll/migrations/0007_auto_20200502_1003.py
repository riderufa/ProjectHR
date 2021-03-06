# Generated by Django 3.0.5 on 2020-05-02 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_auto_20200502_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='наименование опроса')),
                ('time_limit', models.IntegerField(blank=True, null=True, verbose_name='предельное время (сек)')),
                ('date_pub', models.DateField(verbose_name='дата публикации')),
                ('questions', models.ManyToManyField(related_name='polls', through='poll.Kit', to='poll.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_polls', to='poll.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='kit',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll'),
        ),
        migrations.AddField(
            model_name='kit',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Question'),
        ),
    ]
