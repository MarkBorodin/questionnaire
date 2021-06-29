from datetime import timedelta

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from questionnaire.models.survey_template import SurveyTemplate


def in_duration_day():
    return now() + timedelta(days=settings.DEFAULT_SURVEY_PUBLISHING_DURATION)


class Survey(models.Model):

    ALL_IN_ONE_PAGE = 0
    BY_QUESTION = 1
    BY_CATEGORY = 2

    DISPLAY_METHOD_CHOICES = [
        (BY_QUESTION, _("By question")),
        # (BY_CATEGORY, _("By category")),
        (ALL_IN_ONE_PAGE, _("All in one page")),
    ]

    name = models.CharField(_("Name"), max_length=400)
    description = models.TextField(_("Description"), null=True, blank=True)
    is_published = models.BooleanField(_("Users can see it and answer it"), default=True)
    need_logged_user = models.BooleanField(_("Only authenticated users can see it and answer it"))
    editable_answers = models.BooleanField(_("Users can edit their answers afterwards"), default=True)
    display_method = models.SmallIntegerField(
        _("Display method"), choices=DISPLAY_METHOD_CHOICES, default=ALL_IN_ONE_PAGE
    )
    template = models.CharField(_("Template"), max_length=255, null=True, blank=True)
    publish_date = models.DateField(_("Publication date"), blank=True, null=False, default=now)
    expire_date = models.DateField(_("Expiration date"), blank=True, null=False, default=in_duration_day)

    client = models.CharField(max_length=256, null=False, blank=False)
    title = models.CharField(max_length=256, null=False, blank=False)
    slug = models.SlugField(max_length=256, unique=True, null=False, blank=False, verbose_name="URL")
    survey_template = models.ForeignKey(to=SurveyTemplate, null=True, blank=True, on_delete=models.SET_NULL)
    sent = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("survey")
        verbose_name_plural = _("surveys")

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.survey_template is not None:
            survey_template = SurveyTemplate.objects.get(id=self.survey_template.id)
            self.is_published = survey_template.is_published
            self.need_logged_user = survey_template.need_logged_user
            self.editable_answers = survey_template.editable_answers
            self.display_method = survey_template.display_method
            self.publish_date = now()
            self.expire_date = in_duration_day()
        super(self.__class__, self).save(*args, **kwargs)

    @property
    def safe_name(self):
        return self.name.replace(" ", "_").encode("utf-8").decode("ISO-8859-1")

    def latest_answer_date(self):
        """Return the latest answer date.

        Return None is there is no response."""
        min_ = None
        for response in self.responses.all():
            if min_ is None or min_ < response.updated:
                min_ = response.updated
        return min_

    # def get_absolute_url(self):
    #     return reverse("questionnaire:survey-detail", kwargs={"slug": self.slug})

    def non_empty_categories(self):
        return [x for x in list(self.categories.order_by("order", "id")) if x.questions.count() > 0]

    def is_all_in_one_page(self):
        return self.display_method == self.ALL_IN_ONE_PAGE
