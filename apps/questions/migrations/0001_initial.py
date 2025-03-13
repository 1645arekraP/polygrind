import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_tags', models.JSONField(blank=True, null=True)),
                ('ac_rate', models.FloatField()),
                ('content', models.CharField(blank=True, max_length=5012, null=True)),
                ('difficulty', models.CharField(max_length=1024)),
                ('is_paid', models.BooleanField(default=False)),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=1024)),
                ('title_slug', models.SlugField(max_length=255, unique=True)),
                ('pool_tag', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('solved', 'Solved'), ('excelled', 'Excelled'), ('struggled', 'Struggled'), ('unsolved', 'Unsolved'), ('strugglingToSolve', 'StrugglingToSolve')], max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'question', 'relation_type')},
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.CharField(blank=True, default=-1, max_length=12)),
                ('runtime', models.CharField(blank=True, default=-1, max_length=12)),
                ('status', models.CharField(choices=[('has_not_started', 'Has not started'), ('in_progress', 'In progress'), ('solved', 'Solved')], default='has_not_started', max_length=28)),
                ('last_updated', models.CharField(default='inf', max_length=250)),
                ('attempts', models.IntegerField(default=0)),
                ('question', models.ForeignKey(default='two-sum', on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='questions.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'question')},
            },
        ),
    ]
