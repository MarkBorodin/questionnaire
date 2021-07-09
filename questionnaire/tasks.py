from io import StringIO

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.core.mail import EmailMessage
from app.settings import EMAIL_HOST_USER
from questionnaire.models import Survey
import csv
from celery import shared_task

from questionnaire.utils import get_data_for_csv


@shared_task
def send_an_email_about_the_end_of_the_survey(primary_key):
    admins = User.objects.filter(is_superuser=True)
    admins_emails = [admin.email for admin in admins if admin.email]
    survey = get_object_or_404(Survey, pk=primary_key)
    questions_list, answers_list = get_data_for_csv(primary_key)
    csv_file = StringIO()
    writer = csv.writer(csv_file)
    writer.writerow(questions_list)
    writer.writerow(answers_list)

    email = EmailMessage(
        subject=survey.email_text.subject if survey.email_text else f"The client's '{survey.client}' survey results ",
        body=survey.email_text.body if survey.email_text else
        f"""The survey results are in the attached file\nClient: {survey.client}\nTitle: {survey.title}\nName: {survey.name}""", # noqa
        from_email=EMAIL_HOST_USER,
        to=admins_emails,
    )
    email.attach(f'{survey.name}.csv', csv_file.getvalue(), 'text/csv')
    email.send()
