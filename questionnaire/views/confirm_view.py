# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from questionnaire.models import Response
# from questionnaire.utils import send_an_email_about_the_end_of_the_survey
from questionnaire.tasks import send_an_email_about_the_end_of_the_survey


class ConfirmView(TemplateView):

    template_name = "questionnaire/confirm.html"

    def get(self, request, *args, **kwargs):
        response = Response.objects.get(interview_uuid=kwargs["uuid"])
        response_pk = response.survey.pk
        # send_an_email_about_the_end_of_the_survey(response_pk)
        send_an_email_about_the_end_of_the_survey.delay(response_pk)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConfirmView, self).get_context_data(**kwargs)
        context["uuid"] = str(kwargs["uuid"])
        context["response"] = Response.objects.get(interview_uuid=context["uuid"])
        return context
