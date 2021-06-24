import logging
from datetime import date
from functools import wraps

from django.shortcuts import Http404, get_object_or_404

from questionnaire.models import SurveyPlus


def survey_available(func):
    """
    Checks if a survey is available (published and not expired). Use this as a decorator for view functions.
    """

    @wraps(func)
    def survey_check(self, request, *args, **kwargs):
        survey = get_object_or_404(
            SurveyPlus.objects.prefetch_related("questions", "questions__category"), is_published=True, slug=kwargs["slug"]
        )
        if not survey.is_published:
            raise Http404
        if survey.expire_date < date.today():
            msg = "Survey is not published anymore. It was published until: '%s'."
            logging.warning(msg, survey.expire_date)
            raise Http404
        if survey.publish_date > date.today():
            msg = "Survey is not yet published. It is due: '%s'."
            logging.warning(msg, survey.publish_date)
            raise Http404
        return func(self, request, *args, **kwargs, survey=survey)

    return survey_check
