from datetime import timedelta

from django.db import models
from survey.models import Response, Survey, Question, Answer, Category
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.conf import settings


def in_duration_day():
    return now() + timedelta(days=settings.DEFAULT_SURVEY_PUBLISHING_DURATION)


class SurveyTemplate(Survey):

    class Meta:
        verbose_name = "survey template"
        verbose_name_plural = "survey templates"

    def __str__(self):
        return str(f'Template: {self.name}')


class SurveyPlus(Survey):

    client = models.CharField(max_length=256, null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True, verbose_name="URL")
    survey_template = models.ForeignKey(to=SurveyTemplate, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if self.survey_template is not None:
            survey_template = SurveyTemplate.objects.get(name=self.survey_template.name)
            self.is_published = survey_template.is_published
            self.need_logged_user = survey_template.need_logged_user
            self.editable_answers = survey_template.editable_answers
            self.display_method = survey_template.display_method
            self.publish_date = now()
            self.expire_date = in_duration_day()

        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "survey custom"
        verbose_name_plural = "surveys custom"

    def __str__(self):
        return str(self.name)

    # def get_absolute_url(self):
    #     return reverse("survey-detail", kwargs={'survey_slug': self.slug})


class QuestionPlus(Question):

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"
        ordering = ("survey", "order")

    def __str__(self):
        return str(self.text)


class AnswerPlus(Answer):

    def __str__(self):
        return str(self.body)


class ResponsePlus(Response):

    class Meta:
        verbose_name = "Set of answers to surveys custom"
        verbose_name_plural = "Sets of answers to surveys custom"

    def __str__(self):
        return str(self.interview_uuid)


class CategoryPlus(Category):

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name)

