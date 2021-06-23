# -*- coding: utf-8 -*-
from datetime import date

from django.views.generic import TemplateView, ListView

from questionnaire.models import SurveyPlus


# WORKS
class IndexView(ListView):
    template_name = "questionnaire/list.html"
    model = SurveyPlus
    context_object_name = 'surveys'

