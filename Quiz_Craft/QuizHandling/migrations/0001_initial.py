# Generated by Django 3.2.5 on 2021-07-12 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuizTitle', models.CharField(max_length=100)),
                ('Time', models.DurationField(help_text='Duration of the Quizin format HH:MM:SS')),
                ('Score', models.IntegerField(help_text='Total score of the Quiz')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=256)),
                ('student_score', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizHandling.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.IntegerField(default=4, help_text='Score of this question')),
                ('Statement', models.TextField()),
                ('CorrectOption', models.CharField(max_length=1000)),
                ('OtherOption1', models.CharField(max_length=1000)),
                ('OtherOption2', models.CharField(max_length=1000)),
                ('OtherOption3', models.CharField(max_length=1000)),
                ('AuthorKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('QuizKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Q', to='QuizHandling.quiz')),
            ],
        ),
    ]
