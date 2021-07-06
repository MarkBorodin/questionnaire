from io import StringIO

from django.shortcuts import get_object_or_404, redirect
from wkhtmltopdf.views import PDFTemplateView
from django.contrib import messages
import csv

from django.core.mail import EmailMessage
from app.settings import EMAIL_HOST_USER
from questionnaire.models import Survey, Response
from django.conf import settings
import csv
from django.http import HttpResponse
from django.core.mail import send_mail


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


def send_an_email_about_the_end_of_the_survey(primary_key):
    survey = get_object_or_404(Survey, pk=primary_key)
    questions_list, answers_list = get_data_for_csv(primary_key)
    csv_file = StringIO()
    writer = csv.writer(csv_file)
    writer.writerow(questions_list)
    writer.writerow(answers_list)

    email = EmailMessage(
        subject=f"The client's '{survey.client}' survey results ",
        body=f"""The survey results are in the attached file\nClient: {survey.client}\nTitle: {survey.title}\nName: {survey.name}""", # noqa
        from_email=EMAIL_HOST_USER,
        to=['rens2588@gmail.com'],
    )
    email.attach(f'{survey.name}.csv', csv_file.getvalue(), 'text/csv')
    email.send()
