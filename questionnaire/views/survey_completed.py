# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from questionnaire.models import Survey


class SurveyCompleted(TemplateView):

    template_name = "questionnaire/completed.html"

    def get_context_data(self, **kwargs):
        context = {}
        survey = get_object_or_404(Survey, is_published=True, slug=kwargs["slug"])
        context["survey"] = survey
        return context
