# -*- coding: utf-8 -*-
from datetime import date

from django.views.generic import TemplateView, ListView

from questionnaire.models import Survey


# WORKS
class IndexView(ListView):
    template_name = "questionnaire/list.html"
    model = Survey
    context_object_name = 'surveys'

