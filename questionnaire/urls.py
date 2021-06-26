# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path

from questionnaire.utils import GetPDF
from questionnaire.views import ConfirmView, IndexView, SurveyCompleted, SurveyDetail
# from questionnaire.views.survey_result import serve_result_csv

app_name = 'questionnaire'

urlpatterns = [
    path("", IndexView.as_view(), name="survey-list"),
    path("<slug:slug>", SurveyDetail.as_view(), name="survey-detail"),
    path("get_result_pdf/<int:id>", GetPDF.as_view(), name="get_result_pdf"),

    # url(r"^csv/(?P<primary_key>\d+)/", serve_result_csv, name="survey-result"),
    url(r"^(?P<slug>\d+)/completed/", SurveyCompleted.as_view(), name="survey-completed"),
    path("<slug:slug>-<int:step>/", SurveyDetail.as_view(), name="survey-detail-step"),
    url(r"^confirm/(?P<uuid>\w+)/", ConfirmView.as_view(), name="survey-confirmation"),
]
