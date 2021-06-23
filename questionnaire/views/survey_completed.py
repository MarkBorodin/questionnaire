# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from questionnaire.models import SurveyPlus


class SurveyCompleted(TemplateView):

    template_name = "questionnaire/completed.html"

    def get_context_data(self, **kwargs):
        context = {}
        survey = get_object_or_404(SurveyPlus, is_published=True, id=kwargs["id"])
        context["survey"] = survey
        return context