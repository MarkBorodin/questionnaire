import django.dispatch

from django.db.models.signals import post_save
from django.dispatch import receiver

from questionnaire.models import Survey, Question, Response
from questionnaire.models.survey_template import SurveyTemplate

survey_completed = django.dispatch.Signal(providing_args=["instance", "data"])


@receiver(post_save, sender=Survey)
def create_questions_to_survey(sender, instance, created, **kwargs):
    if created:
        if instance.survey_template is not None:
            survey_template = SurveyTemplate.objects.get(id=instance.survey_template.id)
            questions = Question.objects.filter(survey_template=survey_template)
            for question in questions:
                question_new = Question.objects.create(
                    survey=instance,
                    text=question.text,
                    order=question.order,
                    required=question.required,
                    category=question.category,
                    type=question.type,
                    choices=question.choices
                )
                question_new.save()
        instance.survey_template = None
        instance.save()


@receiver(post_save, sender=Response)
def if_completed(sender, instance, created, **kwargs):
    if created:
        survey = Survey.objects.get(id=instance.survey.id)
        survey.completed = True
        if survey.sent is False:
            survey.sent = True
        survey.save()
