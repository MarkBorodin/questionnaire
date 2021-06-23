# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from survey.actions import make_published
from survey.admin import SurveyAdmin, ResponseAdmin, AnswerBaseInline
from survey.exporter.csv import Survey2Csv
from survey.exporter.tex import Survey2Tex
from survey.models import Survey, Response

from questionnaire.models import SurveyPlus, ResponsePlus, QuestionPlus, AnswerPlus, CategoryPlus, SurveyTemplate


class QuestionPlusInline(admin.StackedInline):
    model = QuestionPlus
    ordering = ("order", 'category')
    exclude = ['category']
    extra = 0

    # def get_formset(self, request, survey_obj, *args, **kwargs):
    #     formset = super(QuestionPlusInline, self).get_formset(request, survey_obj, *args, **kwargs)
    #     if survey_obj:
    #         formset.form.base_fields["category"].queryset = survey_obj.categories.all()
    #     return formset


# class CategoryPlusInline(admin.TabularInline):
#     model = CategoryPlus
#     extra = 0


class SurveyPlusAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "need_logged_user")
    list_filter = ("is_published", "need_logged_user")
    # inlines = [CategoryPlusInline, QuestionPlusInline]
    inlines = [QuestionPlusInline]
    actions = [make_published, Survey2Csv.export_as_csv, Survey2Tex.export_as_tex]
    prepopulated_fields = {'slug': ('client', 'title'), }
    exclude = ['display_method', 'template']


class SurveyTemplateAdmin(admin.ModelAdmin):
    list_display = ("name",)
    # list_filter = ("is_published", "need_logged_user")
    inlines = [QuestionPlusInline]
    actions = [make_published, Survey2Csv.export_as_csv, Survey2Tex.export_as_tex]
    # prepopulated_fields = {'slug': ('client', 'title'), }
    exclude = ['display_method', 'template']


# class AnswerPlusBaseInline(admin.StackedInline):
#     fields = ("question", "body")
#     readonly_fields = ("question",)
#     extra = 0
#     model = AnswerPlus


# class ResponsePlusAdmin(admin.ModelAdmin):
#     list_display = ("interview_uuid", "survey", "created", "user")
#     list_filter = ("survey", "created")
#     date_hierarchy = "created"
#     inlines = [AnswerPlusBaseInline]
#     # specifies the order as well as which fields to act on
#     readonly_fields = ("survey", "created", "updated", "interview_uuid", "user")


# class ResponseAdmin(admin.ModelAdmin):
#     list_display = ('client', "interview_uuid", "survey", "created", "user")
#     list_filter = ("survey", "created")
#     date_hierarchy = "created"
#     inlines = [AnswerBaseInline]
#     # specifies the order as well as which fields to act on
#     readonly_fields = ("survey", "created", "updated", "interview_uuid", "user")
#
#     def client(self, obj):  # noqa
#         survey = SurveyPlus.objects.get(id=obj.pk)  # noqa
#         client = survey.client
#         return client


# admin.site.register(Question, QuestionInline)
# admin.site.register(CategoryPlus)
admin.site.register(SurveyPlus, SurveyPlusAdmin)
# admin.site.register(ResponsePlus, ResponsePlusAdmin)
admin.site.register(SurveyTemplate, SurveyTemplateAdmin)


admin.site.unregister(Survey)


class ResponsePlusAdmin(ResponseAdmin):
    list_display = ("client", 'name', 'title', "interview_uuid", 'get_pdf')
    list_filter = ("survey", "created")
    date_hierarchy = "created"
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    readonly_fields = ("survey", "created", "updated", "interview_uuid", "user")

    def client(self, obj):  # noqa
        survey = SurveyPlus.objects.get(id=obj.survey.id)  # noqa
        return survey.client

    def name(self, obj):  # noqa
        survey = SurveyPlus.objects.get(id=obj.survey.id)  # noqa
        return survey.name

    def title(self, obj):  # noqa
        survey = SurveyPlus.objects.get(id=obj.survey.id)  # noqa
        return survey.title

    def get_pdf(self, obj): # noqa
        ...

        return mark_safe(
            f'<a target="_blank" class="button" style="background: purple;"'
            f'href="{reverse("questionnaire:get_result_pdf", args=[obj.pk])}">'
            f'Get result pdf</a>'
        )


admin.site.unregister(Response)
admin.site.register(Response, ResponsePlusAdmin)

