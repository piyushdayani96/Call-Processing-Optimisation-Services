# Generated by Django 2.2.3 on 2019-07-21 12:07

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledgebase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemid', models.CharField(max_length=20)),
                ('problemtext', models.TextField(verbose_name=builtins.max)),
                ('solutiontext', models.TextField()),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificationtext', models.TextField()),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
    ]