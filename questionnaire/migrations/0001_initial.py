# Generated by Django 3.1 on 2021-06-20 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('survey', '0013_auto_20200609_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerPlus',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.answer')),
            ],
            bases=('survey.answer',),
        ),
        migrations.CreateModel(
            name='CategoryPlus',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.category')),
            ],
            bases=('survey.category',),
        ),
        migrations.CreateModel(
            name='QuestionPlus',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.question')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
                'ordering': ('survey', 'order'),
            },
            bases=('survey.question',),
        ),
        migrations.CreateModel(
            name='ResponsePlus',
            fields=[
                ('response_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.response')),
            ],
            options={
                'verbose_name': 'Set of answers to surveys',
                'verbose_name_plural': 'Sets of answers to surveys',
            },
            bases=('survey.response',),
        ),
        migrations.CreateModel(
            name='SurveyPlus',
            fields=[
                ('survey_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.survey')),
                ('client', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'survey',
                'verbose_name_plural': 'surveys',
            },
            bases=('survey.survey',),
        ),
    ]