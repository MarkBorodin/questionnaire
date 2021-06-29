from django.contrib import admin

# from survey.actions import make_published
# from survey.exporter.csv import Survey2Csv
# from survey.exporter.tex import Survey2Tex
from django.urls import reverse
from django.utils.safestring import mark_safe

from questionnaire.models import Answer, Category, Question, Response, Survey
from questionnaire.models.survey_template import SurveyTemplate


class QuestionInline(admin.StackedInline):
    model = Question
    ordering = ("order",)
    exclude = ['category']
    readonly_fields = ['survey', 'survey_template']
    extra = 0

    # def get_formset(self, request, survey_obj, *args, **kwargs):
    #     formset = super().get_formset(request, survey_obj, *args, **kwargs)
    #     if survey_obj:
    #         formset.form.base_fields["category"].queryset = survey_obj.categories.all()
    #     return formset


# class CategoryInline(admin.TabularInline):
#     model = Category
#     extra = 0


class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name", 'client', 'title', 'url_address', 'sent', 'completed', "is_published")
    # list_filter = ("is_published", "need_logged_user")
    # inlines = [CategoryInline, QuestionInline]
    inlines = [QuestionInline]
    # actions = [make_published, Survey2Csv.export_as_csv, Survey2Tex.export_as_tex]
    prepopulated_fields = {'slug': ('client', 'title'), }
    exclude = ['template']
    list_filter = ('client', 'is_published', 'sent', 'completed',)
    search_fields = ['client', 'title', 'name', 'slug', 'description', 'sent', 'completed']
    list_editable = ['sent']
    readonly_fields = ['completed']

    def get_queryset(self, request):
        qs = super(SurveyAdmin, self).get_queryset(request)
        self.request = request # noqa
        return qs

    def url_address(self, obj): # noqa
        address = reverse('questionnaire:survey-detail', kwargs={"slug": obj.slug})
        address = self.request.get_host() + address
        return address


class SurveyTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", )
    # list_filter = ("is_published", "need_logged_user")
    inlines = [QuestionInline]
    # exclude = ['display_method', 'template', 'client', 'title', 'slug']
    exclude = ['template']
    search_fields = ['name', 'description']


class AnswerBaseInline(admin.StackedInline):
    fields = ("question", "body")
    readonly_fields = ("question",)
    extra = 0
    model = Answer


class ResponseAdmin(admin.ModelAdmin):
    list_display = ("client", 'name', 'title', "interview_uuid", 'view_pdf', 'get_pdf')
    list_filter = ("survey", "created")
    date_hierarchy = "created"
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    readonly_fields = ("survey", "created", "updated", "interview_uuid", "user")
    search_fields = ['survey__client', 'survey__title', 'survey__name', 'survey__slug', 'survey__description']

    def client(self, obj):  # noqa
        survey = Survey.objects.get(id=obj.survey.id)  # noqa
        return survey.client

    def name(self, obj):  # noqa
        survey = Survey.objects.get(id=obj.survey.id)  # noqa
        return survey.name

    def title(self, obj):  # noqa
        survey = Survey.objects.get(id=obj.survey.id)  # noqa
        return survey.title

    def view_pdf(self, obj): # noqa
        return mark_safe(
            f'<a target="_blank" class="button" style="background: blue;"'
            f'href="{reverse("questionnaire:view_result_pdf", args=[obj.pk])}">'
            f'View result pdf</a>'
        )

    def get_pdf(self, obj): # noqa
        return mark_safe(
            f'<a target="_blank" class="button" style="background: purple;"'
            f'href="{reverse("questionnaire:get_result_pdf", args=[obj.pk])}">'
            f'Get result pdf</a>'
        )


# admin.site.register(Question, QuestionInline)
# admin.site.register(Category, CategoryInline)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(SurveyTemplate, SurveyTemplateAdmin)

