# Generated by Django 2.2.3 on 2019-07-19 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userzone', '0002_answer_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answeredtype',
            new_name='answeredby',
        ),
    ]
