# Generated by Django 5.1.4 on 2025-01-20 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg_app', '0008_profile_friends_profile_solved_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='solved_questions',
        ),
        migrations.CreateModel(
            name='QuestionRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('solved', 'Solved'), ('excelled', 'Excelled'), ('struggled', 'Struggled'), ('unsolved', 'Unsolved'), ('strugglingToSolve', 'StrugglingToSolve')], max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg_app.profile')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg_app.question')),
            ],
            options={
                'unique_together': {('profile', 'question', 'relation_type')},
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='questions',
            field=models.ManyToManyField(through='pg_app.QuestionRelation', to='pg_app.question'),
        ),
    ]