# Generated by Django 3.2.5 on 2021-07-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizHandling', '0002_alter_quiz_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='done_test',
            field=models.BooleanField(default=False),
        ),
    ]
