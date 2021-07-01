from django.shortcuts import get_object_or_404, redirect
from wkhtmltopdf.views import PDFTemplateView
from django.contrib import messages
from questionnaire.models import Survey, Response
from django.conf import settings
import csv
from django.http import HttpResponse


class GetPDF(PDFTemplateView):
    """get or see pdf file"""
    pk_url_kwarg = 'id'
    template_name = 'questionnaire/view_result_pdf_file.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result_obj_id = self.kwargs['id']
        result_obj = Response.objects.get(id=result_obj_id)
        context['result_obj'] = result_obj
        context['survey'] = Survey.objects.get(id=result_obj.survey.id)

        if 'get_result_pdf' in self.request.build_absolute_uri():
            self.show_content_in_browser = False
        elif 'view_result_pdf' in self.request.build_absolute_uri():
            self.show_content_in_browser = True
        return context


def get_serve_result_csv(request, primary_key):
    """... only if the survey does not require login or the user is logged.

    :param int primary_key: The primary key of the survey."""

    survey = get_object_or_404(Survey, pk=primary_key)
    if not survey.is_published:
        messages.error(request, "This survey has not been published")
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))

    questions = survey.questions.all()
    answers_list = []
    questions_list = []
    for question in questions:
        answer = question.answers_as_text
        answers_list.append(answer[0])
        questions_list.append(question.text)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment;filename={survey.name}.csv"
    writer = csv.writer(response)

    writer.writerow(questions_list)
    writer.writerow(answers_list)

    return response
