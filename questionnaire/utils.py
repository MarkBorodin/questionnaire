from io import StringIO

from django.shortcuts import get_object_or_404
from wkhtmltopdf.views import PDFTemplateView
import base64
from django.core.mail import EmailMessage
from app.settings import EMAIL_HOST_USER
from questionnaire.models import *
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

        f = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)] # noqa
        context['questions_blocks'] = f(context['survey'].questions.all(), result_obj.number_of_responses_per_page)

        if 'get_result_pdf' in self.request.build_absolute_uri():
            self.show_content_in_browser = False
        elif 'view_result_pdf' in self.request.build_absolute_uri():
            self.show_content_in_browser = True
        return context


def get_data_for_csv(primary_key):
    survey = get_object_or_404(Survey, pk=primary_key)
    questions = survey.questions.all()
    answers_list = []
    questions_list = []
    for question in questions:
        answer = question.answers_as_text
        answers_list.append(answer[0])
        questions_list.append(question.text)
    return questions_list, answers_list


def get_survey_result_csv(request, primary_key):
    survey = get_object_or_404(Survey, pk=primary_key)
    questions_list, answers_list = get_data_for_csv(primary_key)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment;filename={survey.name}.csv"
    writer = csv.writer(response)
    writer.writerow(questions_list)
    writer.writerow(answers_list)
    return response


def image_to_code(image):
    data = open(f'media/{image}', 'rb').read()  # read bytes from file
    data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
    data_base64 = data_base64.decode()    # convert bytes to string
    html = '<img src="data:image/png;base64,' + data_base64 + '" id="p1img1">'   # embed in html
    return html
