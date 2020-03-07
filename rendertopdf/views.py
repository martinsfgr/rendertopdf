from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from config.utils import render_to_pdf

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('template.html')
        context = {}
        html = template.render(context)
        pdf = render_to_pdf('template.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            return response
        return HttpResponse("Not Found")