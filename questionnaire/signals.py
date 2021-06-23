import django.dispatch

from django.db.models.signals import post_save
from django.dispatch import receiver
from survey.models import Response, Question

from questionnaire.models import ResponsePlus, SurveyPlus, QuestionPlus

survey_completed = django.dispatch.Signal(providing_args=["instance", "data"])


@receiver(post_save, sender=SurveyPlus)
def invoice_update(sender, instance, created, **kwargs):
    if created:
        if instance.survey_template is not None:
            questions = Question.objects.filter(survey=instance.survey_template)
            for question in questions:
                question_new = QuestionPlus.objects.create(
                    survey=instance,
                    text=question.text,
                    order=question.order,
                    required=question.required,
                    category=question.category,
                    type=question.type,
                    choices=question.choices
                )
                question_new.save()

