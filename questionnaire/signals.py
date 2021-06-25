import django.dispatch

from django.db.models.signals import post_save
from django.dispatch import receiver
# from survey.models import Response, Question

from questionnaire.models import Survey, Question
from questionnaire.models.survey_template import SurveyTemplate

survey_completed = django.dispatch.Signal(providing_args=["instance", "data"])


@receiver(post_save, sender=Survey)
def invoice_update(sender, instance, created, **kwargs):
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
