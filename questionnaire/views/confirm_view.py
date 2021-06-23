# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from questionnaire.models import ResponsePlus


class ConfirmView(TemplateView):

    template_name = "questionnaire/confirm.html"

    def get_context_data(self, **kwargs):
        context = super(ConfirmView, self).get_context_data(**kwargs)
        context["uuid"] = str(kwargs["uuid"])
        context["response"] = ResponsePlus.objects.get(interview_uuid=context["uuid"])
        return context
