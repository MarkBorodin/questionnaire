# Generated by Django 3.1 on 2021-06-22 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_auto_20200609_0748'),
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyTemplate',
            fields=[
                ('survey_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.survey')),
            ],
            options={
                'verbose_name': 'survey template',
                'verbose_name_plural': 'survey templates',
            },
            bases=('survey.survey',),
        ),
        migrations.AlterModelOptions(
            name='categoryplus',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='responseplus',
            options={'verbose_name': 'Set of answers to surveys custom', 'verbose_name_plural': 'Sets of answers to surveys custom'},
        ),
        migrations.AlterModelOptions(
            name='surveyplus',
            options={'verbose_name': 'survey custom', 'verbose_name_plural': 'surveys custom'},
        ),
        migrations.AlterField(
            model_name='surveyplus',
            name='client',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='surveyplus',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='surveyplus',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='surveyplus',
            name='survey_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='questionnaire.surveytemplate'),
        ),
    ]
