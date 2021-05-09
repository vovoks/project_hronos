from django.shortcuts import render
from django.views.generic import TemplateView


class RegisterServiceView(TemplateView):
    template_name = "schedule/register_service.html"
