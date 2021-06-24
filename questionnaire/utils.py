from survey.models import Response
from wkhtmltopdf.views import PDFTemplateView

from questionnaire.models import SurveyPlus


class GetPDF(PDFTemplateView):
    """get or see pdf file"""
    pk_url_kwarg = 'id'
    template_name = 'questionnaire/view_result_pdf_file.html'
    show_content_in_browser = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result_obj_id = self.kwargs['id']
        result_obj = Response.objects.get(id=result_obj_id)
        context['result_obj'] = result_obj
        context['survey'] = SurveyPlus.objects.get(id=result_obj.survey.id)
        return context
